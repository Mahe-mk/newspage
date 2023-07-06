import React, { useState } from 'react';
import {Form , Button} from 'react-bootstrap';

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}


const SignupForm = () => {
  const [form, setForm] = useState({
    username: '',
    email: '',
    password1: '',
    password2: '',
    first_name: '',
    last_name: '',
  });
  const handleChange = (event) => {
    const { name, value } = event.target;
    setForm((prevForm) => ({
      ...prevForm,
      [name]: value,
    }));
  };
  const handleSubmit = (event) => {
    event.preventDefault();
    fetch('http://127.0.0.1:8000/signup/', {                
      method: 'POST',
      body: JSON.stringify(form),
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
      },  
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Registration failed');
        }
        if (response.redirected && response.url.includes('/signin')){
          window.location.href = response.url;
        }else{
          console.error("Registrarion Failed: Invalid data");
        }
        // }`
        // // Redirect the user to the login page
        // window.location.href = '/signin';
      })
      .catch((error) => {
        console.error(error);
      });
  };
  console.log(form);
  return (
 <div className="d-flex justify-content-center align-items-center">
 <Form onSubmit={handleSubmit} className="mx-auto" >
 <Form.Label htmlFor="first_name">First name:</Form.Label>
        <Form.Control
          type="text" id="First_name" name="first_name"
          value={form.first_name}
          placeholder= "First_name"
          onChange={handleChange}
        />
        <Form.Label htmlFor="Last_name">Last name:</Form.Label>
        <Form.Control
          type="text" id="last_name" name="last_name"
          value={form.last_name}
          placeholder= "Last_name"
          onChange={handleChange}
        />
        <Form.Label htmlFor="username" >Username:</Form.Label>
        <Form.Control
          type="text" id="username" name="username" value={form.username}
          placeholder= "Username"onChange={handleChange}
        />
        <Form.Label htmlFor="email">Email:</Form.Label>
        <Form.Control
          type="email" id="email" name="email"
          value={form.email}
          placeholder= "Email"
          onChange={handleChange}
        />
        <Form.Label htmlFor="password1">Password:</Form.Label>
        <Form.Control
          type="password" id="password1" name="password1" autocomplete="new-password"
          value={form.password1}
          placeholder= "Password"
          onChange={handleChange}
        />
        <Form.Label htmlFor="password2">Password Confirmation:</Form.Label>
        <Form.Control
          type="password" id="password2" name="password2"
          value={form.password2}
          placeholder= "Re-Type Password"
          onChange={handleChange}
        />
      
<div className='pt-3'>
<Button type="submit">Register</Button>
<p>Already have an account ? <a href="/signin">Signin Instead</a></p>
</div>
    </Form>
    </div>
  );
};
 
export default SignupForm;
