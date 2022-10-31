<template>
 <table>
  <tr>
    <th>first name</th>
    <th>last name</th>
    <th>email</th>
    <th>phone number</th>
  </tr>
  <tr v-for="contact of contacts" >
    <td>{{contact.first_name}} </td>
    <td>{{contact.last_name}}</td>
    <td> {{contact.email}}</td>
    <td>  {{contact.phone_number}}</td>
  </tr>
</table> 
</template>
<script>
import '../../env-config.js'
import axios from "axios"
export default {
    name: "about",
    data() {
        return {
            contacts: []
        }
    },
    mounted: function () {
        axios.get(`${window.PROTOCOL}://${window.IP_API}:${window.PORT_API}/api/contacts`)
            .then(response => (this.contacts = response.data))
            .catch(function (error) {
                console.log(error);
            })
    },

}
</script>