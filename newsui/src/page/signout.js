import React from 'react';

function SignOut() {
  return (
    <div>
      <h2>You have been logged out.</h2>
      <a href="/signin">SignIn for Existing User</a>
      <p><a href="/signup">Register for New User</a></p>
    </div>
  );
}

export default SignOut;
