import{l as c,A as h,_ as i}from"./index-689e3db1.js";const s=c(),m=h("userData",{state:()=>({userData:null}),getters:{fullname(){var t,a,e;return this.userData?`${(t=this.userData)==null?void 0:t.secondname} ${(a=this.userData)==null?void 0:a.firstname} ${(e=this.userData)==null?void 0:e.surname}`:"No data"},role(){var t;return((t=this.userData)==null?void 0:t.role)||"No data"},group(){var t;return((t=this.userData)==null?void 0:t.group)||"No data"},studentCard(){var t;return((t=this.userData)==null?void 0:t.studentCard)||-1},image(){var t;return((t=this.userData)==null?void 0:t.image)||null}},actions:{set(t){this.userData=t},updateImage(t){this.userData={...this.userData,image:t}},invalidate(){this.userData=null},async loadNewPhoto(t,a){const e=t.target.files[0];if(!e.type.startsWith("image/")){s.showError("Загружаемый файл должен быть картинкой");return}const r=new FormData;r.append("image",e);try{const o=await i(()=>import("./api-427152fd.js"),["assets/api-427152fd.js","assets/index-689e3db1.js","assets/index-602d2a1d.css"]);let n=a=="STUDENT"?o.useApiStudentStore():o.useApiCoachStore();const u=await fetch("/media/update-my-picture",{method:"POST",headers:{Authorization:n.token},body:r});if(u.status==200){s.showSuccess("Новое изображение успешно загружено");const d=await u.json();this.updateImage(d.imgName)}else s.showError("Возникла ошибка при загрузке изображения")}catch{s.showError("Возникла ошибка при загрузке изображения")}},async update(t){const{useApiCoachStore:a}=await i(()=>import("./api-427152fd.js"),["assets/api-427152fd.js","assets/index-689e3db1.js","assets/index-602d2a1d.css"]),e=await a().doRequest("/user/edit","PUT",t);this.set(e),s.showSuccess("Данные успешно сохранены")},async changePassword(t,a,e){const r=await i(()=>import("./api-427152fd.js"),["assets/api-427152fd.js","assets/index-689e3db1.js","assets/index-602d2a1d.css"]);await(e=="STUDENT"?r.useApiStudentStore():r.useApiCoachStore()).doRequest("/user/edit-password","PUT",{oldPassword:t,newPassword:a}),s.showSuccess("Пароль успешно изменен")}}});export{m as u};
