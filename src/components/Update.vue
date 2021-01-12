<template>
    <div>
        <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="书名">
                <el-input v-model="form.book_name"></el-input>
            </el-form-item>
            <el-form-item label="价格">
                <el-input v-model="form.price"></el-input>
            </el-form-item>
            <el-form-item label="作者">
                <el-input v-model="form.author"></el-input>
            </el-form-item>
            <el-form-item label="图片">
                <el-input type="date" v-model="form.pic"></el-input>
            </el-form-item>
            <el-form-item label="出版社">
                <el-input v-model="form.publish"></el-input>
            </el-form-item>
            <el-form-item label="日期">
                <el-input v-model="form.create_time"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit">提交</el-button>
                <el-button>取消</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
export default {
    name: "Update",
    data() {
        return {
            form: {
                book_name: '',
                price: '',
                author: '',
                pic: '',
                publish: '',
                create_time: '',
            }
        }
    },
    methods: {
        onSubmit() {
            this.$axios({
                url:"http://127.0.0.1:8000/lastapp/book/",
                method:"patch",
                data:{
                    book_name:this.form.book_name,
                    price:this.form.price,
                    author:this.form.author,
                    pic:this.form.pic,
                    publish:this.form.publish,
                    create_time:this.form.create_time
                },
            }).then(response=>{
                this.$router.push("/user")
            }).catch(error=>{

            });
        }
    }
}
</script>

<style scoped>

</style>
