import React, { useState, useEffect } from 'react';
import axios from 'axios';

function FavCategories() {
	const [favCategories, setFavCategories] = useState([]);

	useEffect(() => {
	  async function fetchFavCategories() {
		const response = await axios.get('http://127.0.0.1:8000/my-categories');
		setFavCategories(response.data);
	  }
	  fetchFavCategories();
	}, []);
		
console.log(FavCategories);
  return (
    <div>
	{favCategories.map((category) => (
    <main className="container mt-3 mb-5">
	<h3 className="border-bottom pb-1 my-4">List of My Favourite News:</h3>	
	<div className="card mb-4 shadow">
	  <div className="row no-gutters">
	    <div className="col-md-3">
            <img 	src="/media/{{news.image}}" className="card-img-top" />
	    </div>
	    <div className="col-md-8">
	      <div className="card-body">
	        <h5 className="card-title">news.title</h5>
	        <p className="card-text">news.detail</p>
	        <p className="card-text"><a href="/detail/{{news.id}}" className="btn btn-sm btn-success">Read Full</a></p>			
	      </div>
	    </div>
	  </div>
    </div>	
</main>
	))}
    </div>
  )
}

export default FavCategories

