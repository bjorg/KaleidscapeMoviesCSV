# Kaleidescape Movies & Invoices CSV Script (Python)


## Setup

The following commands clone and setup the Python environment for the script.

```shell
git clone https://github.com/bjorg/KaleidscapeMoviesCSV.git
cd KaleidscapeMoviesCSV
python -m venv .venv
```


## Get Movies

First log into the Kaleidescape webstore. Use the browser development tools to get the value of the `STORE_PROD_SESSION_ID` cookie.

Second, run the following commands to get the list of all movies on the account:
```shell
source .venv/Scripts/activate
python kaleidescape-movies-as-csv.py
```

Enter the `STORE_PROD_SESSION_ID` cookie value. 

If successful, the script will generate a `kaleidescape-movies.csv` file.


## Get Invoices

First log into the Kaleidescape webstore. Then go to _Manage_ > _Account_ > _Purchase History_. Once you see your purchase history, use the browser development tools to get the value of the `STORE_PROD_SESSION_ID` cookie.

Second, run the following commands to get the list of all invoices on the account:
```shell
source .venv/Scripts/activate
python kaleidescape-invoices-as-csv.py
```

Enter the `STORE_PROD_SESSION_ID` cookie value.

If successful, the script will generate a `kaleidescape-invoices.csv` file.


## License

> Licensed under the Apache License, Version 2.0 (the "License");
> you may not use this file except in compliance with the License.
> You may obtain a copy of the License at
>
> http://www.apache.org/licenses/LICENSE-2.0
>
> Unless required by applicable law or agreed to in writing, software
> distributed under the License is distributed on an "AS IS" BASIS,
> WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
> See the License for the specific language governing permissions and
> limitations under the License.
