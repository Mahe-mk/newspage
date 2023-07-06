	import React, { useState, useEffect } from 'react';
	import axios from 'axios';
	import { setData } from "../app-data";
	import { Button, Card, Col, NavLink, Row } from "react-bootstrap";


	function FavCategories() {
	const [favCategories, setFavCategories] = useState([]);

	useEffect(() => {
		async function fetchFavCategories() {
		try {
			const token = localStorage.getItem('token');
			const response = await axios.get('http://localhost:8000/my-categories', {
			headers: {
				Authorization: `Bearer ${token}`,
			},
			});
			setFavCategories(response.data);
		} catch (error) {
			console.error('Error fetching favorite categories:', error);
		}
		}
		fetchFavCategories();
	}, []);
	async function signIn() {
		try {
		const response = await axios.post('http://localhost:8000/signin/', {
		});
		const { success, token } = response.data;
		if (success) {	
			localStorage.setItem('token', token);
			console.log('Stored token:', token);
		}
		return success;
		} catch (error) {
		console.error('Error signing in:', error);
		throw error;
		}	
	}
	useEffect(() => {
		signIn('Siva', 'Mahesh@123'); 
	}, []);
	const handleClick =(id)=>{
		setData("selectedNewsId",id)
	}
	return (
		<div>
		<h3 className="border-bottom pb-1 my-4">List of My Favourite News:</h3>
		{favCategories.map((category) => (
			<main className="container mt-3 mb-5" key={category.id}>
			<Card className="card mb-4 shadow">
				<Row className="row no-gutters">
				<Col className="col-md-3">
					<Card.Img src={category.image} className="card-img-top" alt="Category" />
				</Col>
				<Col className="col-md-8">
					<Card.Body className="card-body">
					<Card.Title className="card-title">{category.title}</Card.Title>
					<Card.Text className="card-text">{category.detail}</Card.Text>
					<Button variant="success" size="sm"  href="/detail"  onClick={()=>handleClick(category.id)}>Read Full</Button>
					</Card.Body>
				</Col>
				</Row>
			</Card>
			</main>
		))}
		</div>
	);
	}

	export default FavCategories;


