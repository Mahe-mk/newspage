import React from 'react'

function Fav_Categories() {
  return (
    <div>
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
    </div>
  )
}

export default Fav_Categories