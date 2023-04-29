import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Button, NavLink } from "react-bootstrap";
import { setData } from "../app-data";


function CategoryList() {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    async function fetchCategories() {
      const response = await axios.get('http://localhost:8000/all-category');
      setCategories(response.data);
    }
    fetchCategories();
  }, []);

  const handleClick =(id)=>{
    setData("selectedCategoryId",id)
  }
  return (
    <div>
      <h3>All Categories:</h3>
      {categories.map((category) => (
        <div key={category.id}>
          <h4>{category.title}</h4>
          <img src={'http://localhost:8000' + category.category_image} alt={category.title} height={400} width={600} />
          <p>
            {/* <a href={'/category/' + category.id} className="btn btn-success">
              All News
            </a> */}
            <Button className="btn btn-sm btn-success" href="/categorynews"  onClick={()=>handleClick(category.id)}>Full News</Button>

          </p>
        </div>
      ))}
    </div>
  );
}
export default CategoryList;
