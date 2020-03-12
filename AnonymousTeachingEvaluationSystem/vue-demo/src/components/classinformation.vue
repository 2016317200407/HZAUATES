<template>
<div>

    <h5>您搜索的{{ classname }}老师如下</h5>
     <div v-for="teacher in teachers" :key="teacher.teachername">
        <a :href ="'http://0.0.0.0/teacherinformation/'+ teacher.teachername + '/'">教师姓名：{{ teacher.teachername }}</a>
        <h5>课程：{{ teacher.teacherclass }}</h5>
        <h5>是否是教授：
            <nobr v-if="teacher.isprofessor">
                是
            </nobr>
            <nobr v-else>
                否
            </nobr>
        </h5>
        <h5>
            有 {{teacher.countisroll_call}} 的人认为这个老师喜欢点名
        </h5>
        <h5>
            有 {{teacher.countisquality}} 的人认为这个老师教学质量好
        </h5>
        <h5>
            有 {{teacher.countishighscore}} 的人认为这个老师给分高
        </h5>
        <h5>
            有 {{teacher.countisfunny}} 的人认为这个老师上课有意思
        </h5>
        <h5>
            有 {{teacher.countisrecommend}} 的人认为这个老师值得被你选
        </h5>
        <hr>
    </div>
</div>
</template>
<script>
export default {
    data() {
        return {
            teachers:[]
        }
    },
    mounted(){
        this.$axios
            .get("http://127.0.0.1:8000/homepage/classinformation/"+this.$route.params.classname)
            .then(response=>{
                this.teachers = response.data
                })
            .catch(function (error) { // 请求失败处理
                alert(error)
            })
    }
}
</script>