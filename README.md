## Expense Tracker
Simple CLI expense tracker on Python.
### Installing
Fork repository and clone it to your device:
``` bash
git clone https://github.com/thefirsthouse/expense-tracker.git
```
or download and unarchieve ZIP-file.
### Using
#### Add expense
``` bash
python main.py add --description Milk --amount 100
```
- `--description` - description of record, required
- `--amount`: amount of record, required
#### Delete expense
``` bash
python main.py delete --id 2
```
- `--id` - id of record you want to delete, required
#### Show records
``` bash
python main.py list
```
#### Summary expenses
``` bash
python main.py summary
```
##### Summary expenses by month
``` bash
python main.py summary --month 2
```
- `--month` - expenses will be summarized by this month, type the calendar number of the month
---
Based on: https://roadmap.sh/projects/expense-tracker