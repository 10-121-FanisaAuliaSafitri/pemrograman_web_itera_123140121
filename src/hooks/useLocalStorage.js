import { useState, useEffect } from 'react';

// Fungsi helper untuk mendapatkan nilai awal dari localStorage
function getStorageValue(key, defaultValue) {
  const saved = localStorage.getItem(key);
  try {
    const initial = saved ? JSON.parse(saved) : defaultValue;
    return initial;
  } catch (e) {
    console.error("Gagal parse localStorage", e);
    return defaultValue;
  }
}

export const useLocalStorage = (key, defaultValue) => {
  const [value, setValue] = useState(() => {
    return getStorageValue(key, defaultValue);
  });

  // Effect ini akan berjalan setiap kali 'value' atau 'key' berubah
  useEffect(() => {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch (e) {
      console.error("Gagal menyimpan ke localStorage", e);
    }
  }, [key, value]);

  return [value, setValue];
};