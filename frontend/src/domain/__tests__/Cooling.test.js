import { describe, it, expect } from 'vitest';
import { CoolingItem, CoolingResult } from '../Cooling.js';

describe('Domain - Cooling Logic', () => {
  it('should instantiate CoolingItem correctly', () => {
    const itemData = {
      position: 1,
      time: 3,
      temperature: 72,
      tempDifferential: 8,
      ambientDifferential: 22
    };

    const item = new CoolingItem(itemData);

    expect(item.position).toBe(1);
    expect(item.time).toBe(3);
    expect(item.temperature).toBe(72);
    expect(item.tempDifferential).toBe(8);
    expect(item.ambientDifferential).toBe(22);
  });

  it('should instantiate CoolingResult and map its items correctly', () => {
    const rawItems = [
      {
        position: 0,
        time: 0,
        temperature: 80,
        tempDifferential: 0,
        ambientDifferential: 30
      }
    ];

    const result = new CoolingResult({
      constantK: -0.1034,
      items: rawItems
    });

    expect(result.constantK).toBe(-0.1034);
    expect(result.items.length).toBe(1);
    expect(result.items[0]).toBeInstanceOf(CoolingItem);
    expect(result.items[0].temperature).toBe(80);
  });
});
