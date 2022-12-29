/**
 * Deep copy an object, NOTE: this will not work with circular references/functions
 */
const deepCopy = <T>(obj: T): T => {
  return JSON.parse(JSON.stringify(obj));
};

export default deepCopy;
