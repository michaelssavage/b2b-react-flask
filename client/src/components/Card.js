import React from 'react';
import { Card } from 'react-bootstrap';
import Button from 'react-bootstrap/Button'
import Link from '@material-ui/core/Link';

const productCard = ({ product }) => {

    return (
        <>
            <Card className='my-3 p-3 rounded text-center shadow p-3 mb-5 bg-white rounded' style={{ border: 'none' }}>


                <Card.Body className={`${product.name} rounded text-black`}>

                        <Card.Title as='div'>
                            {product.name.charAt(0).toUpperCase() + product.name.slice(1)}
                        </Card.Title>

                        <Card.Text> 
                            Stock Quantity: {product.stock_quantity}
                        </Card.Text>

                        <Card.Text> 
                            Monthly Restock Date: {product.monthly_restock_date}
                        </Card.Text>

                        <Card.Text> 
                            Restock Quantity: {product.restock_quantity}
                        </Card.Text>

                </Card.Body>
                <div className="pt-2">
                    <Link href="products" color="inherit">
                        <Button variant="info">Order!</Button>   
                    </Link>
                </div>
            </Card>
        </>
    )
}

export default productCard;