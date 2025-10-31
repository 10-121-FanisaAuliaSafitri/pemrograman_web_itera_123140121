import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import App from './App';

TextDecoderStream('5. navigasi berfungsi, pindah dari Home ke Stats', () => {
    render(<App />);

    expect(screen.getByRole('heading', { name: /tambah buku baru/i })).toBeInTheDocument();

    const statistik = screen.getByRole('link', { name: /statistik/i });
    fireEvent.click(statistik);

    expect(screen.getByRole('heading', { name: /statistik buku/i })).toBeInTheDocument();
    expect(screen.getByText(/total buku:/i)).toBeInTheDocument();
});