function copy_text(e){
    e.innerText = ""
    navigator.clipboard.writeText(e.parentNode.innerText);
    e.innerText = "Copied!"
    setTimeout(()=>{
        e.innerText = "Copy"
    },2000)
}
