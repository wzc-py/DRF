<template>
    <div>
        <el-container>
            <el-header>百知书籍信息管理</el-header>
            <el-main><el-table :data="book_list" border style="width: 100%">
                <el-table-column  prop="id" label="ID" width="60"></el-table-column>
                <el-table-column prop="book_name" label="书名" width="120"></el-table-column>
                <el-table-column prop="price" label="价格" width="60"></el-table-column>
                <el-table-column label="作者" width="90">
                    <template slot-scope="scope">
                        <el-popover trigger="hover" placement="top" v-for="(author,index) in scope.row.author_list" :key="index">
                            <p>作者: {{ author.author_name}}</p>
                            <p>年龄: {{ author.age }}</p>
                            <div slot="reference" class="name-wrapper">
                                <el-tag size="medium">{{ author.author_name }}</el-tag>
                            </div>
                        </el-popover>
                    </template>
                </el-table-column>
                <el-table-column prop="publish_name" label="出版社" width="120"></el-table-column>
                <el-table-column label="日期" width="180">
                    <template slot-scope="scope">
                        <i class="el-icon-time"></i>
                        <span style="margin-left: 10px">{{scope.row.create_time}}</span>
                    </template>
                </el-table-column>
                <el-table-column prop="publish_address" label="出版社地址" width="120"></el-table-column>
                <el-table-column label="操作">
                    <template slot-scope="scope">
                        <el-button size="mini" type="danger" @click="handleAdd(scope.$index, scope.row.id)">增加</el-button>
                        <el-button size="mini" type="danger" @click="handleCheck(scope.$index, scope.row.id)">查看</el-button>
                        <el-button size="mini" type="danger" @click="handleEdit(scope.$index, scope.row.id)">修改</el-button>
                        <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row.id)">删除</el-button>
                    </template>
                </el-table-column>
            </el-table></el-main>
        </el-container>
    </div>

</template>

<script>
export default {
    name: "Book",
    methods: {
        handleAdd() {
            this.$router.push("/add");
        },
        handleCheck(index, row) {
            console.log(index, row);
            this.$router.push("/user_de/"+row+"/");
        },
        handleEdit(index,row){
            console.log(index,row);
            this.$router.push("/update/"+row+"/");
        },
        handleDelete(index,row){
            console.log(index,row);
            this.$axios({
                url:"http://127.0.0.1:8000/lastapp/book/"+row+"/",
                method:"delete",
                data:{
                    id:row
                },
            }).then(rst=>{
                console.log(rst.data)
                alert(rst.data.message)
            }).catch(error=>{
                console.log(error)
            })
        }
    },


    data() {
        return {
            book_list: [],
        }
    },
    created() {
        this.$axios({
            url:"http://127.0.0.1:8000/lastapp/book/",
            method:"get",
        }).then(rst=>{
            console.log(rst.data);
            this.book_list=rst.data;
        }).catch(error=>{
            console.log(error);
        })
    }

}
</script>

<style scoped>
.el-header, .el-footer {
    background-color: mediumaquamarine;
    color: #333;
    text-align: center;
    line-height: 30px;
}

.el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
}

.el-main {
    background-color: lightsteelblue;
    color: #333;
    text-align: center;
    line-height: 60px;
}

body > .el-container {
    margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
    line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
    line-height: 320px;
}
</style>
