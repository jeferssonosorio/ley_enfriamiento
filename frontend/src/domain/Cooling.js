export class CoolingItem {
  constructor({ position, time, temperature, tempDifferential, ambientDifferential }) {
    this.position = position;
    this.time = time;
    this.temperature = temperature;
    this.tempDifferential = tempDifferential;
    this.ambientDifferential = ambientDifferential;
  }
}

export class CoolingResult {
  constructor({ constantK, items }) {
    this.constantK = constantK;
    this.items = items.map(item => new CoolingItem(item));
  }
}
