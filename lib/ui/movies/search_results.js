const data = [
  {
    "title": "The Other Guys",
    "img": "https://occ-0-990-987.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABU7kEZ-aNP_qu6FKgoJeOrrVGd84sHKJGqXOBqLw2bO0hbjZ27cL3aTf16tlaK6zhaVCOj9BLZNpZKNKCqTDFqr6plmLCNK1sPo.jpg?r=ecd",
    "link_to_watch": "https://www.netflix.com/watch/70127228?tctx=0%2C0%2C%2C%2C%2C%2C1d28f93e-56d8-4b8b-a9a7-d07d9e171ae6-75181921%7C1%2C%2C"
  },
  {
    "title": "War Dogs",
    "img": "https://occ-0-990-987.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABb7vL3afMXB-Waxz783kH4eqLs8BVOdLpAbkdqgBbr4V5B0oHqF06gStghce1muvmtXZIe3Z7TMzyVU2XIYLrB1eDiGA0YL5aVI.jpg?r=55a",
    "link_to_watch": "https://www.netflix.com/watch/80080359?tctx=0%2C4%2C%2C%2C%2C%2C1d28f93e-56d8-4b8b-a9a7-d07d9e171ae6-75181921%7C1%2C%2C"
  },
  {
    "title": "Red Notice",
    "img": "https://occ-0-990-987.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABf4BpdDVBXrLcPtw9zaQ0pR_kBJTjr-jTLYl189gKVBdGkrX7tIO3VHCJUOOdeS50yZy0BwG6_UGud4YNvljwqoD9VWp5hPVS3AZTS8eoF9XQD2YpZMA6UadWxwwEbIaDnuk.jpg?r=407",
    "link_to_watch": "https://www.netflix.com/watch/81161626?tctx=0%2C8%2C%2C%2C%2C%2C1d28f93e-56d8-4b8b-a9a7-d07d9e171ae6-75181921%7C1%2C%2C"
  },
  {
    "title": "Get Smart",
    "img": "https://occ-0-990-987.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABZyqq6Su9zi3yEGOvAH06SEclGyYHtphXeK2Vqu0z5_TMlWHmkixrs_40hbbQ03hU3VhskPD0EaW4ERDKiLxnxwoFrK3SoKBfjk.jpg?r=450",
    "link_to_watch": "https://www.netflix.com/watch/70077557?tctx=0%2C12%2C%2C%2C%2C%2C1d28f93e-56d8-4b8b-a9a7-d07d9e171ae6-75181921%7C1%2C%2C"
  },
  {
    "title": "Big Daddy",
    "img": "https://occ-0-990-987.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABUIUZyMsDbexWb5HYuhmQHJD-0CSkFQGn83Jj1QMyPcmnwgaqAe1zvhNDiMa8ii7Yh1AUDTOVMOsuo5e1zd5XlHoeKYSuO5jBFQ.jpg?r=e22",
    "link_to_watch": "https://www.netflix.com/watch/21303955?tctx=0%2C16%2C%2C%2C%2C%2C1d28f93e-56d8-4b8b-a9a7-d07d9e171ae6-75181921%7C1%2C%2C"
  },
  {
    "title": "The Do-Over",
    "img": "https://occ-0-990-987.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABdHIp3ZljeB5lzAhI41YXprsXqWzz0kOK9JPOoQwH81s7dOWKctmxWmN2QLBzwTii2RpBxK6BI1jZtkRb-0Ktqf9NldpcgirxkBIrcVU3QymDpOUBMkpVk33o7sOMvnkyZDV.jpg?r=390",
    "link_to_watch": "https://www.netflix.com/watch/80063265?tctx=0%2C20%2C%2C%2C%2C%2C1d28f93e-56d8-4b8b-a9a7-d07d9e171ae6-75181921%7C1%2C%2C"
  },
  {
    "title": "Police Academy",
    "img": "https://occ-0-990-987.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABXT7KRQePInJC461a8wD4OZbbS8e8hqd-27D_REvn4cPT12nkrhH4ETj3iTkCii2-l-8gawLSiKpLEuvv4a9uWSckUhNlJe8knA.jpg?r=d65",
    "link_to_watch": "https://www.netflix.com/watch/60035683?tctx=0%2C24%2C%2C%2C%2C%2C1d28f93e-56d8-4b8b-a9a7-d07d9e171ae6-75181921%7C1%2C%2C"
  },
  {
    "title": "Cop Out",
    "img": "https://occ-0-990-987.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABbVDLqk26uIpzyjBrIG6L1rZYIwyYm0FTONomKf59Kn1pFufWbhZ83C9-7WVEO5RMOY5SKJR-JIi7TRsL5SCPVFxvhAofI5KZPQ.jpg?r=cef",
    "link_to_watch": "https://www.netflix.com/watch/70121092?tctx=0%2C28%2C%2C%2C%2C%2C1d28f93e-56d8-4b8b-a9a7-d07d9e171ae6-75181921%7C1%2C%2C"
  },
  {
    "title": "Here Comes the Boom",
    "img": "https://occ-0-990-987.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABYj8g3_rTUthuyPaz1KKJYI2BONACr1e3zadD9sBsngrQXkHracePOhHjep0kWXQQCLTaQTQrTBZZWKboBXECKRsgVOyhfTOFgA.jpg?r=23e",
    "link_to_watch": "https://www.netflix.com/watch/70217915?tctx=0%2C32%2C%2C%2C%2C%2C1d28f93e-56d8-4b8b-a9a7-d07d9e171ae6-75181921%7C1%2C%2C"
  },
  {
    "title": "Hustle",
    "img": "https://occ-0-990-987.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABZ5GOU4TA3UfTpT_Emuv8M2h2KhgDSNHFmcwo9pzNKcYhTXpkzQ8A92PYY_umrEOv8UWAVYbFAov9mm5bqZNHOok89tTB2X8y_SspKuWHZ9KmGgM5Gb8nI1PaJEy9ieK8t7B.jpg?r=e26",
    "link_to_watch": "https://www.netflix.com/watch/80242342?tctx=0%2C36%2C%2C%2C%2C%2C1d28f93e-56d8-4b8b-a9a7-d07d9e171ae6-75181921%7C1%2C%2C"
  },
  {
    "title": "Death at a Funeral",
    "img": "https://occ-0-990-987.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABZa_pRxUdfy7vgWpmSn-flzfA0lV9VRAyF-cUWgFgLAQ53NIlk-RORVeojakmYGnjfiWtpxn3558T3aOYAV4JILkPZxj-0DcFM8.jpg?r=176",
    "link_to_watch": "https://www.netflix.com/watch/70118780?tctx=0%2C40%2C%2C%2C%2C%2C1d28f93e-56d8-4b8b-a9a7-d07d9e171ae6-75181921%7C1%2C%2C"
  },
  {
    "title": "Tower Heist",
    "img": "https://occ-0-990-987.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABe6MAhOAU6wd-XHeGRQqeJOsF2MPjTvTXkpcZlNHDOW95BQXdeQZq2Bl1-WCOgF59qlq4vF6nxbVqZVrgBw-y9atj_0-6DYe6C_KHBBdGbVV6jyXsX0zNoD63uwGtQZepfU1bomfcVs2yJmzcx7urYulHaZKYLebrI0.jpg?r=7e0",
    "link_to_watch": "https://www.netflix.com/watch/70202145?tctx=0%2C44%2C%2C%2C%2C%2C1d28f93e-56d8-4b8b-a9a7-d07d9e171ae6-75181921%7C1%2C%2C"
  }
]