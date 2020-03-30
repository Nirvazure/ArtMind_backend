import axios from "axios";
import qs from "qs";
import baseURL from "./configUrl.js";

function baseRequest(method, path, params, data, type) {
  method = method.toUpperCase() || "GET";
  let url = "";
  let paramsobj = { params: params };
  if (type === "msg") {
    url = baseURL.onbaseURL;
  } else {
    url = baseURL.baseURL;
  }
  axios.defaults.baseURL = url;
  if (method === "POST") {
    axios.defaults.headers.post["Content-Type"] =
      "application/x-www-form-urlencoded";
    return axios.post(path, qs.stringify(data));
  } else if (method === "GET") {
    return axios.get(path, paramsobj);
  } else {
    return axios.delete(path, qs.stringify(data));
  }
}

//获取所有类别
export let get_style = params => {
  return baseRequest("GET", "/style/all/", params, "");
};


//获取分析结果
export let get_all_painter = params => {
  return baseRequest("GET", "/analyse/"+params.img_id+params.model_id, params, "");
};
//根据id获取画家信息
export let get_all_img = function get_all_img(params) {
  return baseRequest("GET", "/painter/" + params.painter_id, params, "");
};
//根据画家id获取该画家的作品
export let get_img = function get_all_img(params) {
  return baseRequest("GET", "/craft/" + params.painter_id, params, "");
};
//根据分类获取流派图片
export let get_img = function get_all_img(params) {
  return baseRequest("GET", "/craft/" + params.style, params, "");
};
