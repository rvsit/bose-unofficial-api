import { readFile } from 'fs/promises';
import WebsocketSession from './websocketSession';

const main = async () => {
  const configString = await readFile('./config.json', 'utf8');
  const config = JSON.parse(configString);
  if (!config.jwtToken || !config.ip) {
    throw new Error('Invalid config.json');
  }

  const session = await WebsocketSession.create(config.ip, config.jwtToken);

  const nowPlayingRes = await session.socketSend('GET', '/content/nowPlaying');
  console.log('now playing', nowPlayingRes.body);

  const volumeRes = await session.socketSend('GET', '/audio/volume');
  console.log('volume', volumeRes.body);

  const batteryRes = await session.socketSend('GET', '/system/battery');
  console.log('battery', batteryRes.body);
};

main();
