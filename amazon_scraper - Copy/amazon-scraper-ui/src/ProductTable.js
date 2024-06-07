import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import Spinner from './Spinner';

const ProductTable = ({ category }) => {
  const [products, setProducts] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [productsPerPage] = useState(10);
  const [loading, setLoading] = useState(false);

  const baseURL = process.env.NODE_ENV === 'production' ? '' : 'http://localhost:5000';

  useEffect(() => {
    if (category) {
      setLoading(true);
      axios.get(`${baseURL}/api/${category}.json`)
        .then(response => {
          setProducts(response.data);
          setCurrentPage(1);
          setLoading(false);
        })
        .catch(error => {
          console.error('Error fetching the data', error);
          setLoading(false);
        });
    }
  }, [category, baseURL]);

  const indexOfLastProduct = currentPage * productsPerPage;
  const indexOfFirstProduct = indexOfLastProduct - productsPerPage;
  const currentProducts = products.slice(indexOfFirstProduct, indexOfLastProduct);

  const handleNextPage = () => {
    if (currentPage < Math.ceil(products.length / productsPerPage)) {
      setCurrentPage(currentPage + 1);
    }
  };

  const handlePreviousPage = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1);
    }
  };

  if (loading) {
    return <Spinner />;
  }

  return (
    <div>
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Title</TableCell>
              <TableCell align="right">Total Reviews</TableCell>
              <TableCell align="right">Price</TableCell>
              <TableCell align="right">Image</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {currentProducts.map((product) => (
              <TableRow
                key={product.title}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {product.title}
                </TableCell>
                <TableCell align="right">{product.total_reviews}</TableCell>
                <TableCell align="right">{product.price}</TableCell>
                <TableCell align="right">
                  <img src={product.image_url} alt={product.title} width="50" />
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
      <div style={{ marginTop: '10px', display: 'flex', justifyContent: 'center' }}>
        <Button
          variant="contained"
          color="primary"
          onClick={handlePreviousPage}
          disabled={currentPage === 1}
          style={{ marginRight: '10px' }}
        >
          Previous
        </Button>
        <Button
          variant="contained"
          color="primary"
          onClick={handleNextPage}
          disabled={currentPage === Math.ceil(products.length / productsPerPage)}
        >
          Next
        </Button>
      </div>
    </div>
  );
};

export default ProductTable;
