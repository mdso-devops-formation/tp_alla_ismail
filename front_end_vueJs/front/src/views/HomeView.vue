<template>
    <div>
    <form>
    <input v-model="first_name" placeholder="first name" />
    <input v-model="last_name" placeholder="last name" />
    <input v-model="email" placeholder="email" />
    <input v-model="phone_number" placeholder="phone_number" />
    <button type="button" v-on:click="postContact()" >submit</button>
    </form>
    </div>
</template>
<script>
import axios from 'axios'
import '../../env-config.js'
export default {
    name: 'home',
    data: () => ({
        first_name:'',
        last_name:'',
        email:'',
        phone_number:''
    }),


    methods: {
        postContact() {
            axios.post(`${window.PROTOCOL}://${window.IP_API}:${window.PORT_API}/api/contacts`, {
                first_name:   this.first_name,
                last_name:    this.last_name,
                email:        this.email,
                phone_number: this.phone_number
            })

       this.$router.push('/about');
        },
    },
}
</script>
