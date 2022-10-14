import './App.css';

import { useState } from 'react';
import Cookies from 'js-cookie';
// import BookList from "./components/BookList";
import LoginForm from "./components/LoginForm";



// function App() {
//   return (
//     <div className="App">
//       const [auth, setAuth] = useState(!!Cookies.get("Authorization"));
//       <LoginForm setAuth={setAuth} />
//     </div>
//   );
// }

function App() {
  const [auth, setAuth] = useState(!!Cookies.get("Authorization"));
  // return <>{auth ? <BookList /> : <LoginForm setAuth={setAuth} />}</>;
  <LoginForm setAuth={setAuth} />
}

export default App;
