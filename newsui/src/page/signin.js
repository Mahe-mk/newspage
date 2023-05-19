// import React, { useState } from 'react';
// import axios from 'axios';
// import { GoogleLogin } from 'react-google-login';
// import {Form , Button} from 'react-bootstrap';

// function SignIn() {
//   const [formData, setFormData] = useState({
//     username: '',
//     password: '',
//   });

//   const handleSubmit = async (event) => {
//     event.preventDefault();
//     try {
//       const response = await axios.post('http://localhost:8000/signin', formData);
//       console.log(response.data);
//     } catch (error) {
//       console.error(error);
//     }
//   };
//   const handleInputChange = (event) => {
//     const { name, value } = event.target;
//     setFormData((prevFormData) => ({
//       ...prevFormData,
//       [name]: value,
//     }));
//   };

//   return (
//     <div className="d-flex justify-content-center align-items-center">
      
//       <Form onSubmit={handleSubmit} className="mx-auto" >
//       <h1>Welcome to SignIn Page</h1>
//         <Form.Label htmlFor="username">Username:</Form.Label>
//         <Form.Control
//           type="text" name="username"placeholder= "Username" value={formData.username} onChange={handleInputChange}
//         />  
//         <Form.Label htmlFor="password">Password:</Form.Label>
//         <Form.Control
//           type="password" name="password" placeholder= "Password" value={formData.password} onChange={handleInputChange}
//         />
//         <div className='pt-3'>
//         <Button type="submit">SignIn</Button></div>
//       <p>Don't have an account? <a href="/signup">Signup here</a></p>
//       <Button  variant="outline-info">
//         {/* <a href='http://localhost:8000/google/login/?next=/'> */}
//         <a href="http://localhost:8000/google/login/%3Fnext=/">
//           <i className="fab fa-google"></i>
//           SignIn with Google
//         </a>
//       </Button>
//         {/* <Button className="btn btn-outline-info">
//           <a href="/google_login">
//             <i className="fab fa-google"></i>
//             SignIn with Google
//           </a>
//         </Button> */}
//       </Form>
//     </div>
//   );
// }
// export default SignIn;







import React, { useState, useEffect  } from 'react';
import axios from 'axios';
import { Form, Button } from 'react-bootstrap';

function SignIn() {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });
 
  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/signin', formData);
      console.log(response.data);
      // Handle successful sign-in, such as redirecting to the home page
    } catch (error) {
      console.error(error);
      // Handle sign-in error, such as displaying an error message
    }
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  console.log(formData);

  return (
    <div className="d-flex justify-content-center align-items-center">
      <Form onSubmit={handleSubmit} className="mx-auto">
        <h1>Welcome to SignIn Page</h1>
        <Form.Group controlId="username">
          <Form.Label>Username:</Form.Label>
          <Form.Control
            type="text"
            name="username"
            placeholder="Username"
            value={formData.username}
            onChange={handleInputChange}
          />
        </Form.Group>
        <Form.Group controlId="password">
          <Form.Label>Password:</Form.Label>
          <Form.Control
            type="password"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleInputChange}
          />
        </Form.Group>
        <Button type="submit">SignIn</Button>
        <p>
          Don't have an account? <a href="/signup">Signup here</a>
        </p>
        <Button variant="outline-info">
          <a href="http://localhost:8000/google/login/%3Fnext=/">
            <i className="fab fa-google"></i>
            SignIn with Google
          </a>
        </Button>
      </Form>
    </div>
  );
}

export default SignIn;