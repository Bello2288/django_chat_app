import './App.css';

import { useState } from 'react';
import Cookies from 'js-cookie';
import RoomList from "./components/RoomList";
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
  // const [auth, setAuth] = useState(!!Cookies.get("Authorization"));
  // return <>{auth ? <BookList /> : <LoginForm setAuth={setAuth} />}</>;
  // <LoginForm setAuth={setAuth} />
  <LoginForm  />
}

export default App;
