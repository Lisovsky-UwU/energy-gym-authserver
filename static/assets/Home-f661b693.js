import{A as Q,d as W,l as X,m as V,r as g,o as Y,a,c as n,b as e,y as $,B as Z,z as q,u as s,e as p,F as U,h as F,f as v,g as b,q as ee,n as _,s as S,w as I,t as c,p as te,k as se}from"./index-d7d45e2a.js";import{_ as le}from"./default_avatar-05943288.js";import{o as oe,S as L,g as ae,i as ne,p as de}from"./mdi-24228410.js";import{U as ie}from"./Input-d296cc94.js";import{L as H}from"./Loading-e76d4d20.js";import{L as D}from"./LoadingSmall-d4448cd8.js";import{u as re,M as T}from"./news-9ed1ee18.js";import{useApiCoachStore as ce}from"./api-a7f55192.js";import{_ as ue}from"./_plugin-vue_export-helper-c27b6911.js";import"./user-f854f47d.js";const M=ce(),pe=Q("visit",{state:()=>({visits:[]}),actions:{async loadForDate(r,d){this.visits=[],this.visits=await M.doRequest("/visit/get","POST",{date:r,time:d})},async updateVisit(r,d){await M.doRequest("/visit/edit","PUT",{id:r,mark:d})},async cancelLesson(r,d){await M.doRequest("/visit/cancel-lesson","POST",{date:r,time:d})}}}),i=r=>(te("data-v-d78c8d4f"),r=r(),se(),r),me={class:"sm:h-full flex flex-col lg:flex-row gap-5 sm:gap-14 min-w-64"},fe={class:"basis-1/2 bg-background rounded-md relative flex flex-col gap-4 p-4 overflow-visible sm:overflow-auto min-h-72 place-items-center"},xe={class:"flex flex-row gap-4"},ve=i(()=>e("option",{value:"16:00"},"16:00",-1)),_e=i(()=>e("option",{value:"17:30"},"17:30",-1)),we=i(()=>e("option",{value:"19:00"},"19:00",-1)),he=i(()=>e("option",{value:"20:30"},"20:30",-1)),ge=[ve,_e,we,he],be={key:0,class:"w-full h-full place-items-center flex justify-center text-xl text-center"},ye={key:1,class:"w-full flex flex-col gap-2"},ke=["onClick"],Ne={class:"text-lg"},Ce=["name","id","onUpdate:modelValue","onChange"],Ve=i(()=>e("option",{value:1},"Присутствует",-1)),Se=i(()=>e("option",{value:2},"Уважительная",-1)),Le=i(()=>e("option",{value:0},"Отсутствует",-1)),$e={key:0,value:3},Ue={key:2,class:"w-full min-h-72 h-full place-items-center gap-3 flex flex-col justify-center text-2xl text-center"},Ie={class:"basis-1/2 flex flex-col bg-background rounded-md min-h-72 relative overflow-auto"},De={key:0,class:"w-full h-full place-items-center flex justify-center text-xl text-center"},Te={key:1,class:"p-4 gap-4 flex flex-col"},Me={class:"new-block-forward flex flex-rol"},Oe=i(()=>e("br",null,null,-1)),je=i(()=>e("div",{class:"grow"},null,-1)),Be=["onClick"],qe={key:2,class:"w-full min-h-72 h-full place-items-center gap-3 flex flex-col justify-center text-2xl text-center"},Fe={key:3,class:"grow"},He=["disabled"],Re={class:"flex flex-col gap-6 pt-5 px-6 pb-3 rounded-md bg-background"},Ae=i(()=>e("span",{class:"text-2xl"}," Вы уверены что хотите удалить новость? ",-1)),Pe={class:"flex place-content-center gap-2"},ze=["disabled"],Ee=["disabled"],Ge={class:"flex flex-col gap-5 pt-5 rounded-md bg-background"},Je={class:"flex flex-row px-6 gap-6"},Ke={key:0,src:le,alt:"default_avatar",class:"h-44"},Qe={key:1,class:"circle-image"},We=["src"],Xe={class:"flex flex-col gap-3 text-left text-xl justify-center"},Ye={class:"flex flex-col gap-6 pt-5 px-6 pb-3 rounded-md bg-background"},Ze=i(()=>e("span",{class:"text-2xl"}," Вы уверены что хотите отменить занятие? ",-1)),et={class:"flex place-content-center gap-2"},tt=["disabled"],st=["disabled"],lt=W({__name:"Home",setup(r){const d=re(),R=X(),w=pe();let o=V({visits:!0,news:!0,cancelLesson:!1,createNew:!1,deleteNew:!1});const x=g(!1),y=g(!1),k=g(!1);let m=V({});const O=g(-1),f=V({date:new Date().toJSON().slice(0,10),time:"16:00"}),A={0:"bg-red-600",1:"bg-green-600",2:"bg-yellow-500",3:"bg-slate-500"},N=g("");Y(()=>{C(),j()});function C(){o.visits=!0,w.loadForDate(f.date,f.time).finally(()=>{o.visits=!1})}function P(u){m=V(u),y.value=!0}async function z(u,l){await w.updateVisit(u,l)}function j(){o.news=!0,d.loadGymNews("COACH").finally(()=>{o.news=!1})}function E(){const u=N.value.trim();if(!u){R.showError("Введите текст новости");return}o.createNew=!0,d.create(u).then(()=>{N.value=""}).finally(()=>{o.createNew=!1})}function G(u){O.value=u,x.value=!0}function J(){o.deleteNew=!0,d.delete(O.value).then(()=>{x.value=!1,j()}).finally(()=>{o.deleteNew=!1})}function K(){o.cancelLesson=!0,w.cancelLesson(f.date,f.time).then(()=>{k.value=!1,C()}).finally(()=>{o.cancelLesson=!1})}return(u,l)=>(a(),n(U,null,[e("div",me,[e("div",fe,[e("div",xe,[$(e("input",{class:"bg-second text-white p-3 rounded-md shadow-md",type:"date",id:"start",name:"trip-start","onUpdate:modelValue":l[0]||(l[0]=t=>f.date=t),onChange:l[1]||(l[1]=t=>C())},null,544),[[Z,f.date]]),$(e("select",{class:"text-white rounded-md py-2 px-4 bg-second shadow-md","onUpdate:modelValue":l[2]||(l[2]=t=>f.time=t),onChange:l[3]||(l[3]=t=>C())},ge,544),[[q,f.time]])]),s(o).visits?(a(),n("div",be,[p(H)])):s(w).visits.length>0?(a(),n("div",ye,[e("button",{class:"bg-slate-500 px-4 py-2 rounded-md transition-all text-white",onClick:l[4]||(l[4]=t=>k.value=!0)},"Отменить занятие"),(a(!0),n(U,null,F(s(w).visits,t=>(a(),n("div",{key:t.id,class:"flex gap-2"},[e("div",{class:"entry-block grow cursor-pointer",onClick:h=>P(t)},[e("span",Ne,c(t.user.secondname)+" "+c(t.user.firstname)+" "+c(t.user.surname),1)],8,ke),$(e("select",{class:_(`text-white rounded-md p-1 shadow-md ${A[t.mark]}`),name:`visit-${t.id}`,id:`visit-${t.id}`,"onUpdate:modelValue":h=>t.mark=h,onChange:h=>{var B;return z(t.id,Number((B=h.target)==null?void 0:B.value))}},[Ve,Se,Le,t.mark==3?(a(),n("option",$e,"Отменено")):b("",!0)],42,Ce),[[q,t.mark]])]))),128))])):(a(),n("div",Ue,[p(s(L),{class:"text-primary h-20 w-20",type:"mdi",path:s(oe)},null,8,["path"]),v(" На данный день отсутствуют записи студентов ")]))]),e("div",Ie,[s(o).news?(a(),n("div",De,[p(H)])):s(d).gymNews.length>0?(a(),n("div",Te,[(a(!0),n(U,null,F(s(d).gymNews,t=>(a(),n("div",{key:t.id,class:"new-block-back"},[e("div",Me,[e("div",null,[v(" От: "+c(t.createTime)+" ",1),Oe,v(" "+c(t.body),1)]),je,e("button",{title:"Удалить объявление",class:"hover:bg-white hover:bg-opacity-15 transition-all rounded-md px-2",onClick:h=>G(t.id)},[p(s(L),{class:"h-6 w-6",type:"mdi",path:s(ae)},null,8,["path"])],8,Be)])]))),128))])):(a(),n("div",qe,[p(s(L),{class:"text-tertiary h-20 w-20",type:"mdi",path:s(ne)},null,8,["path"]),v(" Объявления отсутствуют ")])),s(o).news?b("",!0):(a(),n("div",Fe)),s(o).news?b("",!0):(a(),n("form",{key:4,class:"w-full bg-second flex flex-row py-3 px-3 rounded-b-md",onSubmit:l[6]||(l[6]=ee(t=>E(),["prevent"]))},[p(ie,{placeholder:"Текст объявления",modelValue:N.value,"onUpdate:modelValue":l[5]||(l[5]=t=>N.value=t),class:"w-full text-lg"},null,8,["modelValue"]),e("button",{disabled:s(o).createNew,type:"submit",class:_(["text-white p-3 ml-3 rounded-md transition-all",s(o).createNew?"":"hover:bg-white hover:bg-opacity-15"])},[s(o).createNew?(a(),S(D,{key:0})):(a(),S(s(L),{key:1,class:"h-8 w-8",type:"mdi",path:s(de)},null,8,["path"]))],10,He)],32))])]),p(T,{modelValue:x.value,"onUpdate:modelValue":l[9]||(l[9]=t=>x.value=t)},{default:I(()=>[e("div",Re,[Ae,e("div",Pe,[e("button",{disabled:s(o).deleteNew,class:_(["text-white text-xl px-6 py-2 rounded-md transition-all bg-red-600",s(o).deleteNew?"":"hover:bg-red-400"]),onClick:l[7]||(l[7]=t=>J())},[s(o).deleteNew?(a(),S(D,{key:0})):b("",!0),v(" Удалить ")],10,ze),e("button",{disabled:s(o).deleteNew,class:_(["text-white text-xl px-6 py-2 rounded-md transition-all bg-second",s(o).deleteNew?"":"hover:bg-slate-600"]),onClick:l[8]||(l[8]=t=>x.value=!1)}," Отмена ",10,Ee)])])]),_:1},8,["modelValue"]),p(T,{modelValue:y.value,"onUpdate:modelValue":l[11]||(l[11]=t=>y.value=t)},{default:I(()=>[e("div",Ge,[e("div",Je,[s(m).user.image==null?(a(),n("img",Ke)):(a(),n("div",Qe,[e("img",{src:"/media/"+s(m).user.image},null,8,We)])),e("div",Xe,[e("span",null,"Студенческий: "+c(s(m).user.studentCard),1),e("span",null,c(s(m).user.secondname)+" "+c(s(m).user.firstname)+" "+c(s(m).user.surname),1),e("span",null,"Группа: "+c(s(m).user.group),1)])]),e("button",{class:"w-full bg-second text-white rounded-b-md text-xl py-3",onClick:l[10]||(l[10]=t=>y.value=!1)},"Закрыть")])]),_:1},8,["modelValue"]),p(T,{modelValue:k.value,"onUpdate:modelValue":l[14]||(l[14]=t=>k.value=t)},{default:I(()=>[e("div",Ye,[Ze,e("div",et,[e("button",{disabled:s(o).cancelLesson,class:_(["text-white text-xl px-6 py-2 rounded-md transition-all bg-red-600",s(o).cancelLesson?"":"hover:bg-red-400"]),onClick:l[12]||(l[12]=t=>K())},[s(o).cancelLesson?(a(),S(D,{key:0})):b("",!0),v(" Да ")],10,tt),e("button",{disabled:s(o).cancelLesson,class:_(["text-white text-xl px-6 py-2 rounded-md transition-all bg-second",s(o).cancelLesson?"":"hover:bg-slate-600"]),onClick:l[13]||(l[13]=t=>x.value=!1)}," Нет ",10,st)])])]),_:1},8,["modelValue"])],64))}});const ft=ue(lt,[["__scopeId","data-v-d78c8d4f"]]);export{ft as default};
