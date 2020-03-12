<template>
  <div id="App">
    <h2>华中农业大学匿名教评系统</h2>输入你要查询的老师名字或者课程名字：
    <input tpye="text" name="searchname" v-model="torcname"/>
    <br />
    <div class="choose">
      <div class="radio-box" v-for="(item,index) in radios" :key="item.id">
        <span class="radio" :class="{'on':item.isChecked}"></span>
        <input
          v-model="radio"
          :value="item.value"
          class="input-radio"
          :checked="item.isChecked"
          @click.native="check(index)"
          type="radio"
        />
        {{item.label}}
      </div>
    </div>
    <button v-on:click="login()">登陆</button>
  </div>
</template>
<script>
export default {
  data() {
    return {
    radio: 'teachername',
    radios:[
      {
        label: '教师',
        value:'teachername',
        isChecked: true,
      },
      {
        label: '课程',
        value:'classname',
        isChecked: false,
      }
    ]
    }
  },
  methods: {
    check(index) {
    this.radios.forEach((item) => {
      item.isChecked = false;
    })
    this.radio = this.radios[index].value;
    this.radios[index].isChecked = true;
    },
    login:function(){
      if (!this.torcname) {
          alert("输入内容不能为空")
      } else {
        if (this.radio == 'teachername') {
          this.$router.push({
            path: "/teacherinformation/" + this.torcname
          })
        }
        else{
          this.$router.push({
            path:"/classinformation/" + this.torcname
          })
        }
      }
    }
  }
}
</script>