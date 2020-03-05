# Swagger入門(1)_SwaggerHub


## 1. 為何需要Swagge

前端技術和後端技術在各自的道路上越走越遠。  
前端和後端的唯一聯系，變成了API接口；API文檔變成了前後端開發人員聯系的紐帶，變得越來越重要，`swagger`就是一款讓你更好的書寫API文檔的框架。


## 2. 認識Swagger生態


Swagger的主要工具包括：

-   Swagger編輯器–基於瀏覽器的編輯器，您可以在其中編寫OpenAPI定義。
    
-   Swagger UI –將OpenAPI定義呈現為交互式API文檔，例如[http://petstore.swagger.io上的](http://petstore.swagger.io/)文檔。
    
-   Swagger Codegen –基於OpenAPI定義生成服務器代碼和客戶端庫。


其中，紅顏色的是`swaggger`官網方推薦的。

![](https://img-blog.csdn.net/20170827202033991?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvaTY0NDgwMzg=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

下面再細看看swagger的生態的具體內容：

### swagger-ui

這玩意兒從名字就能看出來，用來顯示API文檔的。和`rap`不同的是，它不可以編輯。

![技術分享圖片](https://img-blog.csdn.net/20170827190923413?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvaTY0NDgwMzg=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

點擊某個詳細API的可以試。

![Imgur](https://i.imgur.com/oT464V4.png)

### swagger-editor

就是一個在線編輯文檔說明文件（swagger.json或swagger.yaml文件）的工具，以方便生態中的其他小工具（swagger-ui）等使用。  
左邊編輯，右邊立馬就顯示出編輯內容來。  
![Imgur](https://i.imgur.com/ASfjEwj.png)

編輯swagger說明文件使用的是`yaml`語法具體的內容可以去官網查看。

### 各種語言版本的根據annotation或者註釋生成swagger說明文檔的工具

目前最流行的做法，就是在代碼註釋中寫上swagger相關的註釋，然後，利用小工具生成swagger.json或者swagger.yaml文件。

目前官方沒有推出。github上各種語言各種框架各種有，可以自己搜吧搜吧，這裏只說一個php相關的。  
`swagger-php`  :https://github.com/zircote/swagger-php

### swagger-validator

這個小工具是用來校驗生成的文檔說明文件是否符合語法規定的。用法非常簡單，只需url地址欄，根路徑下加上一個參數url，參數內容是放swagger說明文件的地址。即可校驗。  
例如：  
![Imgur](https://i.imgur.com/pH6rcxw.png)  
docker hub地址為：https://hub.docker.com/r/swaggerapi/swagger-validator/  
可以pull下鏡像來自己玩玩。

### swagger-codegen

代碼生成器，腳手架。可以根據swagger.json或者swagger.yml文件生成指定的計算機語言指定框架的代碼。  
有一定用處，Java系用的挺多。工業上應該不咋用。

### mock server

這個目前還沒有找到很合適的mock工具，包括rap也好，其他API文檔工具也好，都做的不夠完善，大多就是根據說明文件，例如swagger.json等生成一些死的靜態的mock數據，不能夠根據限定條件：例如“只能是數字，必傳”等做出合理的回應。

## 3. 使用SwaggerHub

### 最基本的yaml
```yaml
swagger: '2.0'
info:
  version: '1.0.0'
  title: 'test2'
  description: 'sample test2'
paths: {}  #`paths`部分中，您可以定義API操作。我們稍後將填充它
```

### 添加服務器訊息與定義GET操作

假設我們的API用於管理用戶列表。每個用戶都有一個ID，API需要進行操作以按其ID返回用戶。那將是一個像這樣的GET請求：

```js
GET /users/3
GET /users/15

```

使用Swagger，我們可以如下描述此GET操作。中的`{userId}`部分`/users/{userId}`指示path參數，即可以變化的URL組件。

```yaml
swagger: '2.0'
info:
  version: '1.0.0'
  title: 'test2'
  description: 'sample test2'
  
  
servers:
  - url: https://api.example.com/v1 #我們需要定義API服務器地址和API調用的基本URL
  

paths:
  /users/{userId}:
    get:
      summary: Returns a user by ID
      responses:
        '200':
          description: OK

```

![](https://images2.imgbox.com/ff/c9/oq30mpmC_o.png)

### 定義參數

- 我們的API操作`GET /users/{userId}`具有`userId`用於指定要返回的用戶ID 的參數。要在您的規範中定義此參數，請添加以下`parameter`部分
- 發現剛剛創立時，不是openapi版本，導致一直出現error。
```yaml
openapi: 3.0.0
info:
  version: "1.0.0-oas3"
  title: test2
  description: sample test2
servers:
  - url: 'https://api.example.com/v1'
paths:
  '/users/{userId}':
    get:
      summary: Returns a user by ID
      parameters:
        - name: userId
          in: path
          required: true
          description: The ID of the user to return
          schema:
            type: integer
      responses:
        '200':
          description: OK



```

![Imgur](https://i.imgur.com/Fs4KMZC.png)


### 定義響應

- 假設成功調用`GET /users/{userId}`返回HTTP狀態200和以下JSON對象：

```json
{
  "id": 42,
  "name": "Arthur Dent"
}
```

- 請`content`在200響應下添加以下部分。該`content`部分指定響應包含JSON數據（`application/json`）。注意`schema`元素–它描述了響應主體的結構，例如返回的JSON對象的屬性。另外，您還可以描述API調用可以返回的各種錯誤代碼。

```yaml
openapi: 3.0.0
info:
  version: "1.0.0-oas3"
  title: test2
  description: sample test2
servers:
  - url: 'https://api.example.com/v1'
paths:
  '/users/{userId}':
    get:
      summary: Returns a user by ID
      parameters:
        - name: userId
          in: path
          required: true
          description: The ID of the user to return
          schema:
            type: integer
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                  name:
                    type: string
        '400':
          description: The specified user ID is invalid (e.g. not a number)
        '404':
          description: A user with the specified ID was not found
```


![Imgur](https://i.imgur.com/JOD7YN2.png)


### 發布API


我們的API已完成，因此我們將其發布。發布是一種告訴人們API處於穩定狀態的方法，它將按設計運行，並可供應用程序使用。不用擔心配置服務器-本教程是關於在沒有實際實現的情況下設計API規範。

要發布API，請單擊您的API版本旁邊的下拉箭頭，然後單擊 ![](https://app.swaggerhub.com/help/_images/buttons/publish.png)。

恭喜你！您已經在SwaggerHub上發布了您的第一個API！您可以從瀏覽器的地址欄中復制其地址，並與他人共享。由於這是公共API，因此擁有鏈接的任何人都可以查看它，並且該鏈接將顯示在SwaggerHub的搜索結果中。如果您的SwaggerHub計劃允許，則可以[將API](https://app.swaggerhub.com/help/apis/public-and-private-apis)設為[私有](https://app.swaggerhub.com/help/apis/public-and-private-apis)。

![Imgur](https://i.imgur.com/OjRw2WK.png)

