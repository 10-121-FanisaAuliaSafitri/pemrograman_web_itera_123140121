import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { BookProvider } from '../../context/BookContext';
import BookForm from './BookForm';

// Mock wrapper untuk menyediakan context
const renderWithProvider = (component) => {
  return render(<BookProvider>{component}</BookProvider>);
};

test('1. Merender form tambah buku dengan benar', () => {
  renderWithProvider(<BookForm />);
  
  expect(screen.getByLabelText(/judul buku/i)).toBeInTheDocument();
  expect(screen.getByLabelText(/penulis/i)).toBeInTheDocument();
  expect(screen.getByRole('button', { name: /simpan buku/i })).toBeInTheDocument();
});

test('2. Menampilkan error jika judul atau penulis kosong saat submit', () => {
  renderWithProvider(<BookForm />);
  
  const submitButton = screen.getByRole('button', { name: /simpan buku/i });
  
  // Submit form dalam keadaan kosong
  fireEvent.click(submitButton);
  
  // Harapkan pesan error muncul
  expect(screen.getByText(/judul dan penulis tidak boleh kosong/i)).toBeInTheDocument();
});