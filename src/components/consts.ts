const constants = {
  WEB_PREFIX: "",
};

if (process.env.NODE_ENV == "internal") {
  constants.WEB_PREFIX = "static/";
}

console.log(
  `Running in ${process.env.NODE_ENV}, setting web prefix to ${constants.WEB_PREFIX}`
);

export default constants;
