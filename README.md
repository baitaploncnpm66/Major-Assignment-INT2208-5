# IntelliPurchase
## Link hệ thống: [link](http://13.238.195.79:8000/)
## Video demo: [link](https://youtu.be/hp9F7mq3mOY)
## Báo cáo dự án: [link](https://drive.google.com/file/d/1p-zcYOKpvo-cXShUTXLi3PdcOfKKkmN_/view?usp=sharing)
## Link dự án trước: [github](https://github.com/baitaploncnpm66/Mobile-e-commerce-review-sentiment-classification)
## Tài liệu về hệ thống:
- Problem Statement: [link](https://drive.google.com/file/d/1ANg4OiaLZVKevgtWIH8ulUIlT_YkzGTN/view?usp=sharing)
- System Glossary: [link](https://drive.google.com/file/d/1TdKHSnemjcRdbc1TrBWnTGDE07S0a6Eo/view?usp=sharing)
- System Specification: [link](https://drive.google.com/file/d/1SZTrhboc5_JfEPXKk0prJZfrG4PyNpD-/view?usp=sharing)
- System Supplementary Specification: [link](https://drive.google.com/file/d/1MR4xCp6HM5yZ6Mi2-einHPb6JLzmWBHk/view?usp=sharing)
- Scenarios, User Stories: [link](https://drive.google.com/file/d/1PZBCHRUaYcgjQMt4uYXhEdk-9FnAKTqa/view?usp=sharing)
- Use-Case Model: [link](https://drive.google.com/file/d/13dpZ632XSWyJG-32SKF2spc7khcHVHBa/view?usp=sharing)
- User Manual: [link](https://drive.google.com/file/d/1u1teAh1m9lAwESrdosInRwbtKSja4uQ3/view?usp=sharing)

# Bài tập lớn môn Công nghệ phần mềm INT2208 5
# Trang web phân tích bán hàng IntelliPurchase

## Thành Viên

1. Bùi Đức Mạnh - 22022602
2. Lê Việt Hùng - 22022666
3. Đàm Thái Ninh - 22022522
4. Trần Nam Anh - 22022569

## Hướng Dẫn Cài Đặt
```
git clone <url>
pip install -r requirements.txt
cd IntelliPurchase
python manage.py migrate
python manage.py runserver
```

## Gitflow
### Được giao task mới
- Pull develop: `git pull origin develop`
- Tạo nhánh mới từ develop: `git checkout -b <tên-branch>`
- Code x3,14
### Đang làm task cũ
- Pull develop về nhánh hiện tại vào mỗi ngày làm việc mới: `git pull origin develop`
- Code x3,14
- Commit và push code lên github mỗi khi kết thúc ngày làm việc:
  - `git add.`
  - `git commit -m "Message"`
  - `git push origin <tên-branch-hiện-tại>`

## Một vài câu lệnh git
- `git clone <url>`: clone repository về máy
- `git add .`: add toàn bộ thay đổi để commit
- `git commit -m "Commit Message"`: commit toàn bộ thay đổi với message chỉ định vào nhánh hiện tại
- `git push origin <tên-branch>`: push toàn bộ commit (tức là sự thay đổi về các file) ở nhánh hiện tại lên nhánh được chỉ định trên github
- `git pull origin <tên-branch>`: lấy toàn bộ commit (tức là sự thay đổi về các file) ở nhánh được chỉ định từ github về nhánh hiện tại
- `git checkout <tên-branch>`: chuyển sang nhánh được chỉ định
- `git checkout -b <tên-branch>`: tạo branch mới và chuyển sang đó (tên branch không được trùng nhau)
- `git branch -d <tên-branch>`: xoá branch được chỉ định khỏi máy (đương nhiên toàn bộ thay đổi có ở nhánh này cũng sẽ mất hết)
- **Nếu không quen có thể sử dụng GUI của VSC**

## Phản hồi và Đóng góp

Chúng tôi cam kết phản hồi và đánh giá mọi yêu cầu từ cộng đồng người dùng. Bất kỳ issues, pull requests hoặc ý kiến đóng góp nào cũng được đánh giá và giải quyết một cách nhanh chóng.

Nếu bạn gặp bất kỳ vấn đề hoặc có ý kiến đóng góp, vui lòng tạo một issue mới hoặc một pull request. Chúng tôi luôn đánh giá cao sự hợp tác của cộng đồng và sẵn lòng cải thiện dự án cùng với bạn.
