import { ulid } from 'ulid';
import { MessageEvent, WebSocket } from 'ws';

export type WebsocketCallback = (data: any) => void;

/**
 * Example response:
  {
    countryCode: 'US',
    defaultName: 'Bose Portable Smart Speaker',
    guid: 'abcdefgh-1234-1234-1234-abcdefghijkl',
    limitedFeatures: false,
    name: 'Speaker',
    productColor: 3,
    productId: 16435,
    productName: 'Bose Portable Smart Speaker',
    productType: 'taylor',
    regionCode: 'XX',
    serialNumber: '123456789012345AB',
    softwareVersion: '13.1.5-13+d13f30d',
    variantId: 3
  }
 */
export interface SystemInfoResponse {
  countryCode: string;
  defaultName: string;
  guid: string;
  limitedFeatures: boolean;
  name: string;
  productColor: number;
  productId: number;
  productName: string;
  productType: string;
  regionCode: string;
  serialNumber: string;
  softwareVersion: string;
  variantId: number;
}

export interface SystemPowerControlResponse {
  power: 'ON' | 'OFF';
}

class WebsocketSession {
  protected productId = ulid();
  protected socket: WebSocket;
  protected requestId = 1;
  protected deviceGuid = '';
  protected expectedResponses: { [key: number]: WebsocketCallback } = {};

  constructor(
    public readonly ip: string,
    protected readonly jwtToken: string,
    protected readonly debug = false,
  ) {
    const url = `wss://${ip}:8082?product=${this.productId}`;
    if (debug) {
      console.log('Connecting to: ', url);
    }
    this.socket = new WebSocket(url, 'eco2', {
      //we get an 'invalid' certificate, maybe in the future check for the actual BOSE certificate
      rejectUnauthorized: false,
      protocolVersion: 13,
    });
    this.socket.onmessage = this.onMessage.bind(this);
  }

  static async create(ip: string, jwtToken: string) {
    const session = new WebsocketSession(ip, jwtToken);
    await session.awaitOpen();
    await session.getSystemInfo();
    return session;
  }

  public async awaitOpen() {
    return new Promise<void>((resolve, reject) => {
      this.socket.on('open', () => resolve());
      this.socket.on('error', err => reject(err));
    });
  }

  private onMessage(message: MessageEvent) {
    var data = JSON.parse(message.data.toString('utf8'));
    if (this.debug) {
      console.debug('Message received: ', data);
    }
    if (data.header && data.header.reqID) {
      const callback = this.expectedResponses[data.header.reqID];
      if (callback) {
        callback(data);
      }
    }
  }

  public async socketSend(method: 'GET' | 'POST', resource: string, body?: any) {
    return new Promise<any>((resolve, reject) => {
      try {
        //timeout after 5 seconds
        const timeout = setTimeout(() => reject(new Error('Request timed out')), 5000);
        this.socketSendCallback(
          method,
          resource,
          data => {
            clearTimeout(timeout);
            resolve(data);
          },
          body,
        );
      } catch (err) {
        reject(err);
      }
    });
  }

  public socketSendCallback(
    method: 'GET' | 'POST',
    resource: string,
    callback?: WebsocketCallback,
    body?: any,
  ) {
    const reqID = ++this.requestId;

    const request = {
      header: {
        resource,
        token: this.jwtToken,
        msgtype: 'REQUEST',
        method,
        device: this.deviceGuid,
        reqID,
      },
      body,
    };

    try {
      const requestString = JSON.stringify(request);
      this.socket.send(requestString);
      if (callback) {
        this.expectedResponses[reqID] = callback;
      }
      return reqID;
    } catch (err) {
      throw new Error(`Error sending request: ${err}`);
    }
  }

  public async getSystemInfo(): Promise<SystemInfoResponse> {
    const response = await this.socketSend('GET', '/system/info');

    this.deviceGuid = response.body.guid;

    return response.body;
  }

  public async getSystemPowerControl(): Promise<SystemPowerControlResponse> {
    const response = await this.socketSend('GET', '/system/power/control');
    return response.body;
  }

  public async setSystemPowerControl(power: 'ON' | 'OFF') {
    await this.socketSend('POST', '/system/power/control', { power });
  }
}

export default WebsocketSession;
