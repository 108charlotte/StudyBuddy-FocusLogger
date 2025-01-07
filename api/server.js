const express = require("express")
const app = express()

app.set('view engine', 'ejs')

app.get("/", (req, res) => {
    console.log("Here")
    res.render("index", {text: "World"})
})

Router.post('/save-time', (req, res) => {
    const { startTime, endTime } = req.body

    if (!startTime || !endTime)
})

const userRouter = require("./routes/users")

app.use("/users", userRouter)

app.listen(3000)
