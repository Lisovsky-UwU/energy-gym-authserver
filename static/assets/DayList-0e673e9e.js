import{L as w}from"./Loading-e038d42b.js";import{M as k}from"./MainBlockLkTemplate-737e69f1.js";import{u as b}from"./entry-bd1a44ee.js";import{d as v,r as p,o as B,a as s,s as L,w as N,c as o,e as S,F as u,h as m,b as e,n as $,t as a,u as x}from"./index-689e3db1.js";import"./_plugin-vue_export-helper-c27b6911.js";import"./api-427152fd.js";import"./user-7dab814b.js";const C={key:0,class:"flex items-center sm:h-full sm:absolute justify-center text-2xl py-6 w-full"},D={key:1,class:"grid grid-cols-1 lg:grid-cols-2 gap-4 p-4"},M={class:"flex flex-col gap-2 grow place-content-center"},F={key:0,class:"relative overflow-x-auto"},T={class:"w-full text-sm text-left rtl:text-right text-gray-400"},E=e("thead",{class:"text-xs uppercase bg-gray-700 text-gray-400"},[e("tr",null,[e("th",{scope:"col",class:"px-5 py-3"}," Студенческий "),e("th",{scope:"col",class:"px-5 py-3"}," ФИО "),e("th",{scope:"col",class:"px-5 py-3"}," Группа ")])],-1),V={scope:"row",class:"px-5 py-3 font-medium whitespace-nowrap text-white"},j={class:"px-5 py-3 text-white"},z={class:"px-5 py-3 text-white"},J={key:1,class:"text-xl text-center text-white py-4"},K=v({__name:"DayList",props:{weekday:String},setup(f){const h={0:"понедельник",1:"вторник",2:"среду",3:"четверг",4:"пятницу",5:"субботу",6:"воскресенье"},y=b();let r=p([]);const n=p(!0),_=f;B(()=>{const[c,i]=new Date().toJSON().slice(0,10).split("-");y.getForDay(Number(_.weekday),`${i}-${c}`).then(l=>{r.value=l}).finally(()=>{n.value=!1})});const g=["16:00","17:30","19:00","20:30"];return(c,i)=>(s(),L(k,{title:`Запись на ${h[c.$props.weekday||0]}`},{default:N(()=>[n.value?(s(),o("div",C,[S(w)])):(s(),o("div",D,[(s(),o(u,null,m(g,(l,d)=>e("div",{key:d,class:"border border-black rounded-md flex flex-col bg-second"},[e("div",{class:$(`w-full text-center text-3xl py-2 text-white bg-select-entry-${d+1}`)},a(l),3),e("div",M,[x(r).filter(t=>t.selectedTime.time==l).length>0?(s(),o("div",F,[e("table",T,[E,e("tbody",null,[(s(!0),o(u,null,m(x(r).filter(t=>t.selectedTime.time==l),t=>(s(),o("tr",{key:t.id,class:"bg-second border-b border-gray-700"},[e("th",V,a(t.user.studentCard),1),e("td",j,a(t.user.secondname)+" "+a(t.user.firstname)+" "+a(t.user.surname),1),e("td",z,a(t.user.group),1)]))),128))])])])):(s(),o("div",J," Записи на данный день нет "))])])),64))]))]),_:1},8,["title"]))}});export{K as default};