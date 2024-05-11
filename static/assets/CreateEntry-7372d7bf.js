import{j as B,S as N}from"./mdi-744fba57.js";import{M as O}from"./MainBlockLkTemplate-b4be1b63.js";import{L as j}from"./Loading-95ec2321.js";import{L as V}from"./LoadingSmall-c082d992.js";import{u as W}from"./entry-114b13de.js";import{A as M,d as F,l as q,r as x,m as w,o as z,a as t,s as k,w as D,c as l,e as S,u,b as f,F as y,h as T,t as b,n as C,g as E,f as G,p as R,k as H}from"./index-13497349.js";import{useApiStudentStore as J}from"./api-c0bedf42.js";import{w as A}from"./Common-47779d4f.js";import{_ as K}from"./_plugin-vue_export-helper-c27b6911.js";import"./user-1ccd504c.js";const P=J(),Q=M("availableTime",{state:()=>({availableTimes:[]}),getters:{mappedAvTimesAboutWeekdays(){const s=[];return this.availableTimes.forEach(a=>{let c=s.find(p=>p.weekday==a.weekday);c===void 0&&(c={id:s.length,weekday:a.weekday,times:[]},s.push(c)),c.times.push(a)}),s},mappedAvTimes(){const s={};return this.availableTimes.forEach(a=>{s[a.id]=a}),s}},actions:{async loadAvailableTimes(){this.availableTimes=await P.doRequest("/avtime/get","GET")}}}),I=s=>(R("data-v-5adffe5e"),s=s(),H(),s),U=I(()=>f("div",{class:"bg-select-entry-1 bg-select-entry-2 bg-select-entry-3 bg-select-entry-4"},null,-1)),X={key:0,class:"flex items-center sm:h-full sm:absolute justify-center text-2xl py-6 w-full"},Y={key:1},Z={class:"grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5 p-4 place-items-stretch pb-[78px]"},ee={class:"text-lg col-span-2"},te=["onClick"],se=["onClick"],ae={key:2,class:"flex flex-col gap-3 items-center sm:h-full sm:absolute justify-center text-2xl py-6 w-full"},oe=I(()=>f("span",{class:"text-center"}," Запись закрыта. Откроется 25 числа. ",-1)),re={key:3,class:"w-full min-h-[68px] absolute bottom-0 bg-second flex flex-row-reverse py-3 pr-3 rounded-b-md"},le=["disabled"],ie=F({__name:"CreateEntry",setup(s){const a=W(),c=Q(),p=q(),g=x(!0),m=x(!1);let r=w({});z(async()=>{try{await a.loadOpen(),a.registrateIsOpen&&await c.loadAvailableTimes()}finally{g.value=!1}});function v(i,n){i in r?n==r[i]?delete r[i]:r[i]=n:Object.keys(r).length>=3?p.showError("Выбрано максимальное количество дней для записи"):r[i]=n}function $(){const i=[];for(var n in r)i.push(r[n]);if(i.length==0){p.showError("Выберите хотя бы одно время для записи");return}m.value=!0,c.loadAvailableTimes().finally(()=>{}),a.createEntries(i).then(e=>{if(e.some(o=>o.error)){let o=e.filter(d=>d.error==!1),h=e.filter(d=>d.error==!0);if(o.length==0)p.showError("Все места на выбранные времена закончились, записи не были созданы",!1);else{let d="Закончились места на времена:<br>";h.forEach(L=>{const _=c.mappedAvTimes[L.selectedTime];d+=`${A[_.weekday]} - ${_.time}<br>`}),d+="На остальные времена вы были записаны",p.showWarning(d,!1)}}else p.showSuccess("Вы успешно были записаны на выбранные времена");r=w({})}).finally(()=>{m.value=!1})}return(i,n)=>(t(),k(O,{title:"Запись в спортзал"},{default:D(()=>[U,g.value?(t(),l("div",X,[S(j)])):u(a).registrateIsOpen?(t(),l("div",Y,[f("div",Z,[(t(!0),l(y,null,T(u(c).mappedAvTimesAboutWeekdays,e=>(t(),l("div",{key:"wd-"+e.id,class:"bg-white shadow-md rounded-md text-center grid grid-cols-2 grid-rows-3 p-4 gap-2 border border-gray-300"},[f("span",ee,b(u(A)[e.weekday]),1),(t(!0),l(y,null,T(e.times,(o,h)=>(t(),l(y,{key:`${e.id}-${o.id}`},[o.available?e.id in u(r)&&o.id==u(r)[e.id]?(t(),l("button",{key:2,class:C("bg-select-entry-"+(h+1)+" w-full py-2 text-white rounded-md text-base font-bold"),onClick:d=>v(e.id,o.id)},b(o.time),11,se)):(t(),l("button",{key:1,class:"w-full py-2 bg-second text-white rounded-md text-base font-bold",onClick:d=>v(e.id,o.id)},b(o.time),9,te)):(t(),l("button",{key:0,class:"w-full py-2 bg-gray-400 text-gray-200 rounded-md text-base font-bold",onClick:n[0]||(n[0]=d=>u(p).showWarning("На выбранное время закончились места"))},b(o.time),1))],64))),128))]))),128))])])):(t(),l("div",ae,[S(u(N),{class:"text-primary h-20 w-20",type:"mdi",path:u(B)},null,8,["path"]),oe])),u(a).registrateIsOpen&&!g.value?(t(),l("div",re,[f("button",{disabled:m.value,class:C(m.value?"bg-tertiary-hover text-white px-12 py-2 rounded-md uppercase text-lg font-semibold":"bg-tertiary text-white px-12 py-2 rounded-md uppercase text-lg font-semibold hover:bg-tertiary-hover transition-all"),onClick:n[1]||(n[1]=e=>$())},[m.value?(t(),k(V,{key:0})):E("",!0),G(" Записаться ")],10,le)])):E("",!0)]),_:1}))}});const ye=K(ie,[["__scopeId","data-v-5adffe5e"]]);export{ye as default};
