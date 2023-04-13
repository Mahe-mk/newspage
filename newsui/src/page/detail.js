import React from 'react'

function Detail() {
  return (
    <div>
        <main className="container mt-3 mb-5">
        <div className="row my-3">
            <div className="col-md-8">
                <div className="card mb-3">
                    <img src="/media/{{news.image}}" className="card-img-top" />
                <div className="card-body">
                    <p className="card-title h1">news.title</p>
                    <hr/>
                    <p className="card-text">news.detail</p>
                </div>
                </div>		
                <p className="card-text"><a href="/all-news" className="btn btn-sm btn-success">Previous Page</a></p>
        </div>	
        </div>
        </main>
        
    </div>
  )
}
export default Detail
