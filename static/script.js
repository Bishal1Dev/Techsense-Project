// ======================================
// Unit Converter
// Author: #Bishal Lamichhane,Arpit Kharel,Dipak Yadav,Bibek Shahi
// ======================================

const valueInput = document.getElementById("value");
const convertBtn = document.getElementById("convertBtn");
const resultBox = document.getElementById("result");
const historyList = document.getElementById("historyList");
const copyBtn = document.getElementById("copyBtn");
const swapBtn = document.getElementById("swapBtn");

let history = [];

convertBtn.addEventListener("click", convert);

async function convert() {

    const value = valueInput.value.trim();

    if (value === "") {
        alert("Please enter a value.");
        return;
    }

    const data = {
        category: category.value,
        from: from.value,
        to: to.value,
        value: value
    };

    try {

        const response = await fetch("/convert", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (!result.success) {
            resultBox.innerHTML = result.message;
            return;
        }

        const text =
            `${value} ${from.value} = ${result.result} ${to.value}`;

        resultBox.innerHTML = text;

        addHistory(text);

    } catch (err) {

        resultBox.innerHTML = "Unable to connect to server.";

    }

}

swapBtn.addEventListener("click", () => {

    let temp = from.value;
    from.value = to.value;
    to.value = temp;

});

copyBtn.addEventListener("click", async () => {

    if (resultBox.innerText === "Result will appear here")
        return;

    try {

        await navigator.clipboard.writeText(resultBox.innerText);

        copyBtn.innerHTML = "Copied ✓";

        setTimeout(() => {

            copyBtn.innerHTML = "Copy Result";

        },1500);

    } catch {

        alert("Copy failed.");

    }

});

function addHistory(item){

    history.unshift(item);

    if(history.length>10)
        history.pop();

    historyList.innerHTML="";

    history.forEach(entry=>{

        let li=document.createElement("li");

        li.innerHTML=entry;

        historyList.appendChild(li);

    });

}

valueInput.addEventListener("keypress",(e)=>{

    if(e.key==="Enter")
        convert();

});