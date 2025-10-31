import { renderHook } from '@testing-library/react';
import { useBookStats } from '../hooks/useBookStats';

const mockBooks = [
  { id: 1, title: 'A', author: 'A', status: 'milik' },
  { id: 2, title: 'B', author: 'B', status: 'milik' },
  { id: 3, title: 'C', author: 'C', status: 'baca' },
  { id: 4, title: 'D', author: 'D', status: 'beli' },
];

test('3. useBookStats menghitung statistik dengan benar', () => {
  const { result } = renderHook(() => useBookStats(mockBooks));
  
  expect(result.current.total).toBe(4);
  expect(result.current.owned).toBe(2);
  expect(result.current.reading).toBe(1);
  expect(result.current.toBuy).toBe(1);
});