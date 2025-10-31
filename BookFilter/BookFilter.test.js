import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
// Impor yang hilang ada di baris ini:
import { BookProvider, useBooks } from '../../context/BookContext'; 
import BookFilter from './BookFilter';

// Komponen helper untuk mengecek nilai context
const TestComponent = () => {
  // Gunakan 'searchTerm', bukan 'searchItem'
  const { searchTerm } = useBooks(); 
  return <div data-testid="search-value">{searchTerm}</div>;
};

test('4. Input pencarian memperbarui nilai searchTerm di context', () => {
  render(
    <BookProvider>
      <BookFilter />
      <TestComponent />
    </BookProvider>
  );

  const searchInput = screen.getByPlaceholderText(/cari buku/i);
  
  fireEvent.change(searchInput, { target: { value: 'Laskar Pelangi' } });
  
  expect(screen.getByTestId('search-value')).toHaveTextContent('Laskar Pelangi');
});