<template>
    <div id="App">
        <h2>教师姓名：{{ teachername }}</h2>
        <h5>课程：{{ teacherclass }}</h5>
        <h5>是否是教授：
            <nobr v-if="isprofessor">
                是
            </nobr>
            <nobr v-else>
                否
            </nobr>
        </h5>
        <h5>
            有 {{countisroll_call}} 的人认为这个老师喜欢点名
        </h5>
        <h5>
            有 {{countisquality}} 的人认为这个老师教学质量好
        </h5>
        <h5>
            有 {{countishighscore}} 的人认为这个老师给分高
        </h5>
        <h5>
            有 {{countisfunny}} 的人认为这个老师上课有意思
        </h5>
        <h5>
            有 {{countisrecommend}} 的人认为这个老师值得被你选
        </h5>
        <hr>
    <br>
        对于{{ teachername }}老师<br>
        我来说两句：<input type="text" id = "evaluation" v-model="saysomething"><br>
        爱点名 是：<input type="checkbox" id = "isroll_call" value="isroll_call" v-model="check">
        教学质量好 是：<input type="checkbox" id = "isquality" value="isquality" v-model="check">
        给分高 是：<input type="checkbox" id = "ishighscore" value="ishighscore" v-model="check">
        上课有趣 是：<input type="checkbox" id = "isfunny" value="isfunny" v-model="check">
        值得推荐给同学们 是：<input type="checkbox" id = "isrecommend" value="isrecommend" v-model="check">
        <button v-on:click="submit()">提交</button>
    <br>
        排序方法
        <button v-on:click="sortbyzxhf()">最新回复</button>
        <button v-on:click="sortbydzl()">点赞量</button>
    <br>
    <div v-for="(evaluation,index) in evaluations" :key="evaluation.timestamp">
        <hr>
        评论时间:{{evaluation.timestamp}}
        <br>
        评论:{{evaluation.teacherevaluation}}
        <br>
        点赞:<button v-on:click="ilike(index)" :id="evaluation.timestamp">{{evaluation.likecount}}</button>
        <br>
        <button v-on:click="jubao(evaluation.timestamp)" :id="evaluation.timestamp">举报</button>
    </div>
    </div>    
</template>
<script>
export default {
    data() {
        return {
            teachername:this.$route.params.username,
            teacherclass:'',
            isprofessor:true,
            countisroll_call:'',
            countisquality:'',
            countishighscore:'',
            countisfunny:'',
            countisrecommend:'',
            evaluations:[{
                timestamp:'',
                teacherevaluation:'',
                likecount:''
            }],
            check:[]
        }
    },
    mounted(){
        this.$axios
            .get("http://127.0.0.1:8000/homepage/teacherinformation/"+this.$route.params.username)
            .then(response=>{
                this.teacherclass=response.data.teacherclass
                this.isprofessor=response.data.isprofessor
                this.countisroll_call=response.data.countisroll_call
                this.countisquality=response.data.countisquality
                this.countishighscore=response.data.countishighscore
                this.countisfunny=response.data.countisfunny
                this.countisrecommend=response.data.countisrecommend
                })
            .catch(function (error) { // 请求失败处理
                alert(error);
            }),
            this.$axios
            .get("http://127.0.0.1:8000/homepage/teacherinformation/evaluation/dzl/"+this.$route.params.username)
            .then(response=>{
                this.evaluations=response.data
                })
            .catch(function (error) { // 请求失败处理
                alert(error);
            })
    },
    methods:{
        submit:function(){
            if (this.saysomething){
                this.$axios({
                url:'http://127.0.0.1:8000/homepage/teacherinformation/',
                method:'post',
                data:{
                    'teachername':this.$route.params.username,
                    'check':this.check,
                    'evaluation':this.saysomething
                }
            })
            .then(response=>{
                alert('评论成功');
            })
            .catch(function(error){
                alert(error);
            })
            }else{
                alert("输入内容不能为空")
            }
            this.$axios
                .get("http://127.0.0.1:8000/homepage/teacherinformation/"+this.$route.params.username)
                .then(response=>{
                    this.teacherclass=response.data.teacherclass
                    this.isprofessor=response.data.isprofessor
                    this.countisroll_call=response.data.countisroll_call
                    this.countisquality=response.data.countisquality
                    this.countishighscore=response.data.countishighscore
                    this.countisfunny=response.data.countisfunny
                    this.countisrecommend=response.data.countisrecommend
                    })
                .catch(function (error) { // 请求失败处理
                    alert(error);
                }),
                this.$axios
                .get("http://127.0.0.1:8000/homepage/teacherinformation/evaluation/dzl/"+this.$route.params.username)
                .then(response=>{
                    this.evaluations=response.data
                    })
                .catch(function (error) { // 请求失败处理
                    alert(error);
                })
        },
        sortbyzxhf:function(){
            this.$axios
            .get("http://127.0.0.1:8000/homepage/teacherinformation/evaluation/zxhf/"+this.$route.params.username)
            .then(response=>{
                this.evaluations=response.data
                })
            .catch(function (error) { // 请求失败处理
                alert(error);
            })
        },
        sortbydzl:function(){
            this.$axios
            .get("http://127.0.0.1:8000/homepage/teacherinformation/evaluation/dzl/"+this.$route.params.username)
            .then(response=>{
                this.evaluations=response.data
                })
            .catch(function (error) { // 请求失败处理
                alert(error);
            })
        },
        ilike:function(i){
            this.$axios
            .get("http://127.0.0.1:8000/homepage/teacherinformation/evaluation/dz/"+this.evaluations[i].timestamp)
            .then(response=>{
                this.evaluations[i].likecount = response.data.likecount
                this.$set(this.evaluations,i,this.evaluations[i])
                })
            .catch(function (error) { // 请求失败处理
                alert(error);
            })
        }
    }
}
</script>