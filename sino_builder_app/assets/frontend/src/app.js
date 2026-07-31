const API="http://127.0.0.1:8000";

function log(txt){

const box=document.getElementById("log");

box.textContent+=txt+"\n";

box.scrollTop=box.scrollHeight;

}

function clearLog(){

document.getElementById("log").textContent="";

}

function sleep(ms){

return new Promise(r=>setTimeout(r,ms));

}

async function buildProject(){

const project=document.getElementById("project").value.trim();

const idea=document.getElementById("idea").value.trim();

if(project===""||idea===""){

alert("املأ جميع الحقول");

return;

}

clearLog();

log("🐉 Sino Builder AI");

log("");

log("🚀 بدء البناء");

log("");

const stages=[

"🧠 تحليل الفكرة",

"📋 إنشاء خطة التنفيذ",

"🏗 إنشاء المعمارية",

"🎨 إنشاء الواجهة",

"⚙ إنشاء Backend",

"🗄 إنشاء قاعدة البيانات",

"🤖 إنشاء الذكاء الاصطناعي",

"🔒 مراجعة الأمان",

"🧪 اختبار المشروع"

];

for(const s of stages){

log(s);

await sleep(400);

}

log("");

log("📡 الاتصال بالمحرك...");

try{

const response=await fetch(API+"/build",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

project_name:project,

requirements:idea

})

});

if(!response.ok){

throw new Error("HTTP "+response.status);

}

const result=await response.json();

log("✅ المحرك استجاب");

log("");

if(result.execution){

log("📋 خطة التنفيذ:");

for(const step of result.execution.pipeline){

log("   ✔ "+step);

await sleep(250);

}

}

log("");

if(result.plan){

log("🧠 المهام:");

for(const task of result.plan.tasks){

log("• "+task);

await sleep(120);

}

}

log("");

if(result.generated){

log("📁 الملفات:");

for(const file of result.generated.generated){

log("📄 "+file);

await sleep(80);

}

}

log("");

if(result.release){

log("📦 Release");

log(result.release.release_file);

}

log("");

log("🎉 اكتمل البناء");

log("");

log("━━━━━━━━━━━━━━━━━━");

log("✅ Sino Builder AI");

log("Project Ready");

log("━━━━━━━━━━━━━━━━━━");

}catch(err){

log("");

log("❌ فشل البناء");

log(err);

}

}

async function loadProjects(){

try{

const response=await fetch(API+"/projects");

if(!response.ok){

return;

}

const data=await response.json();

const container=document.getElementById("projectsList");

if(!container){

return;

}

container.innerHTML="";

for(const project of data){

const div=document.createElement("div");

div.style.padding="12px";

div.style.margin="10px 0";

div.style.background="#1f2937";

div.style.borderRadius="12px";

div.innerHTML="📂 "+project;

container.appendChild(div);

}

}catch(e){

console.log(e);

}

}

window.onload=function(){

const btn=document.getElementById("buildBtn");

if(btn){

btn.onclick=buildProject;

}

loadProjects();

};
