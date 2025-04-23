import logo from "./logo.svg";
import "./App.css";

// import DriveFolderUploadIcon from "@mui/icons-material/DriveFolderUpload";
import React, { useState, useEffect } from "react";

import axios from "axios";

const url = window.location.hostname;
const api = axios.create({
  baseURL: `http://${url}:8000`,
});

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

function App() {
  const [imgs, setimgs] = useState();
  const [res, setRes] = useState();
  const [den, setDen] = useState();

  let upload = async () => {
    const uploaddata = new FormData();

    uploaddata.append("j1", imgs);
    uploaddata.append("j2", imgs);
    uploaddata.append("j3", imgs);
    uploaddata.append("j4", imgs);

    let resp = await api
      .post("predict/", uploaddata)
      .then((resp) => {
        // setRes(resp.data["image"]);
        setDen(resp.data["density"]);
      })
      .catch((err) => {
        alert(err);
      });
  };

  return (
    <div className="app">
      <div className="app2">
        <input
          type="file"
          onChange={(e) => {
            setimgs(e.target.files[0]);
          }}
        />
        <button onClick={upload}>predict</button>

        {/* <button onClick={cam}>Open Web cam</button> */}

        <br />
        {res && (
          <div className="img12">
            {/* <img src={`data:image/jpeg;base64,${res}`} alt="None" /> */}
            <p>{den}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
