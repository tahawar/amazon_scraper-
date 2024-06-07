import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ProductTable from './ProductTable';
import './App.css';

function App() {
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('');

  const baseURL = process.env.NODE_ENV === 'production' ? '' : 'http://localhost:5000';

  useEffect(() => {
    axios.get(`${baseURL}/api/user_queries.json`)
      .then(response => {
        const fetchedCategories = response.data;
        setCategories(fetchedCategories);
        if (fetchedCategories.length > 0) {
          setSelectedCategory(fetchedCategories[0]);
        }
      })
      .catch(error => {
        console.error('Error fetching categories', error);
      });
  }, [baseURL]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Amazon Products</h1>
        <select
          value={selectedCategory}
          onChange={(e) => setSelectedCategory(e.target.value)}
        >
          {categories.map((category, index) => (
            <option key={index} value={category}>
              {category}
            </option>
          ))}
        </select>
        {selectedCategory && <ProductTable category={selectedCategory} />}
      </header>
    </div>
  );
}

export default App;
