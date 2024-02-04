import { Route, Routes } from "react-router";
import Home from "./Home";
import Navbar from "./Navbar";
import Restaurant from "./Restaurant";

function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route exact path="/restaurants/:id" element={<Restaurant/>}></Route>
        <Route exact path="/" element={<Home/>}></Route>
      </Routes>
    </>
  );
}

export default App;
