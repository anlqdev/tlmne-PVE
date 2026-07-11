# Tiến lên Miền Nam (bản đấu với AI)

Tài liệu này tóm tắt **luật chơi** của Tiến lên Miền Nam làm bởi iaminfinityiq

---

## 1) Giới thiệu
- Game có **2 người chơi**. (Bạn là người chơi thứ nhất, còn AI là người chơi thứ hai)
- Hai bên thi đấu trên bản đồ gồm các địa điểm (ô).
- Mỗi bên có **1 triệu quân** ban đầu.
- Mỗi lượt, người chơi có thể:
  - **Nâng cấp** (phòng thủ / sát thương / hiệu suất / kinh tế / hậu cần)
  - Hoặc **di chuyển quân** sang ô kề bên.

---

## 2) Bản đồ và các thủ đô
### Hà Nội (thủ đô P1)
- **Hà Nội**
- **Triệu Sơn 1** ↔ **Triệu Sơn 2**
- **Nông Cống 1** ↔ **Nông Cống 2**
- **Tĩnh Gia 1** ↔ **Tĩnh Gia 2**
- Các tuyến dẫn tới **Quảng Trị**

Sơ đồ (theo code):
```
              --- Hà Nội ---
            /       |        \
Triệu Sơn 1   Nông Cống 1     Tĩnh Gia 1
     |              |              |
Triệu Sơn 2   Nông Cống 2     Tĩnh Gia 2
     |              |              |
 Quảng Trị ------- Huế -------- Đà Nẵng
     |              |              |
  Cờ Đỏ 2      Thới Lai 2       Ô Môn 2
     |              |              |
  Cờ Đỏ 1      Thới Lai 1       Ô Môn 1
          \\         |         /
            ---- Sài Gòn ----
```

### Sài Gòn (thủ đô P2)
- **Sài Gòn**
- **Cờ Đỏ 1** ↔ **Cờ Đỏ 2**
- **Thới Lai 1** ↔ **Thới Lai 2**
- **Ô Môn 1** ↔ **Ô Môn 2**
- Các tuyến dẫn tới **Đà Nẵng** rồi tới vùng trung tâm (Huế/Đà Nẵng).

---

## 3) Khởi tạo quân (xếp phòng thủ ban đầu)
### Lượt của P1 (Hà Nội)
- P1 chọn số quân (tổng tối đa **1.000.000**) để đặt vào:
  - **Triệu Sơn 1**
  - **Nông Cống 1**
  - **Tĩnh Gia 1**
- Phần còn lại sẽ tự động đặt vào **Hà Nội**.

### Lượt của P2 (Sài Gòn)
- P2 chọn số quân (tổng tối đa **1.000.000**) để đặt vào:
  - **Cờ Đỏ 1**
  - **Thới Lai 1**
  - **Ô Môn 1**
- Phần còn lại sẽ tự động đặt vào **Sài Gòn**.

---

## 4) Thuộc tính người chơi
Mỗi người chơi có các chỉ số (ban đầu đều là 1):
- **Phòng thủ** (`hp`)
- **Sát thương** (`melee`)
- **Hiệu suất** (`efficiency`)
- **Kinh tế** (`economy`)
- **Hậu cần** (`supply`)

Ngoài ra:
- **Tiền** (`money`) ban đầu = 0
- **Quân** (`troops`) ban đầu = 1.000.000

---

## 5) Cơ chế lượt chơi
### 5.1. Hiệu suất quyết định số hành động
- Đầu mỗi lượt: `actions = efficiency`.
- Trong khi `actions != 0`:
  - chạy xử lý trận đánh ở mọi ô
  - người chơi chọn hành động
  - nếu hành động “mất lượt” thì giảm action còn lại sau khi thoát khỏi menu hành động nội bộ

> Có 1 hành động được đánh dấu là **không mất action**: “Ghé thăm địa điểm kế bên”.

### 5.2. Trước hành động: giao tranh tự động
Trong `before_action()`:
- Với **tất cả ô**, nếu trong ô đó có quân của **cả hai bên**, thì chiến đấu xảy ra ngay.

Kết quả giao tranh (tóm tắt):
- Mỗi bên gây “hits” dựa trên `hp` và `melee`.
- Số quân bị mất mỗi bên được tính theo tỉ lệ theo hits.
- Nếu tiêu diệt hết quân ở ô, game sẽ thông báo.

---

## 6) Điều kiện thắng thua
### 6.1. Thắng khi chiếm thủ đô đối phương
Trước mỗi hành động, game kiểm tra:
- Nếu **thủ đô của một bên** đã hết quân của bên đó, nhưng đối phương vẫn còn quân tại thủ đô đó ⇒ bên đối phương **giành chiến thắng**.

### 6.2. Hòa nếu cùng lúc cùng thua
- Nếu **cả hai thủ đô** cùng đồng thời rơi vào trạng thái “bị mất hết quân ở bên đó” trong cùng một bước kiểm tra ⇒ **hòa**.

### 6.3. Thắng do không thể hiến tế (khi hết quân)
Trong menu hành động, nếu:
- Người chơi đang quan sát có **0 quân ở ô thủ đô**
- Và `player.troops == 0`
- Mà **`player.supply == 1`**
=> Game tuyên bố đối thủ **thắng** vì người chơi không thể hiến tế để đổi lấy quân.

---

## 7) Các hành động trong lượt
## 7.1. Ghé thăm địa điểm kế bên (không mất action)
- Dùng khi người chơi muốn đổi “ô đang quan sát”.
- Cho phép ghé thăm **các ô kề bên** với ô hiện tại.
- Thao tác này có `lose_action=False` nên **không tiêu hao hành động**.

## 7.2. Nâng cấp (tiêu hao 1 hành động)
Các nâng cấp luôn trừ **tiền** từ `money` và tăng chỉ số tương ứng:

1. **Nâng cấp phòng thủ** (`hp`)
   - Giá ban đầu: 100 (nghìn VND)
   - Mỗi lần tăng giá thêm 100

2. **Nâng cấp sát thương** (`melee`)
   - Giá ban đầu: 100
   - Mỗi lần tăng giá thêm 100

3. **Nâng cấp hiệu suất** (`efficiency`)
   - Giá ban đầu: 500
   - Mỗi lần tăng giá thêm 500

4. **Nâng cấp kinh tế** (`economy`)
   - Giá ban đầu: 600
   - Mỗi lần tăng giá thêm 600

5. **Nâng cấp hậu cần** (`supply`)
   - Giá ban đầu: 500
   - Mỗi lần tăng giá thêm 500

### 7.2.1. Cách tạo tiền
Trong `before_action()`:
- `money += economy * 100`

Tức mỗi vòng lặp trước hành động, kinh tế tạo thêm tiền theo `economy`.

## 7.3. Di chuyển quân tới địa điểm kề bên (tiêu hao 1 hành động)
- Chỉ hiện menu nếu trong **ô đang quan sát** có quân của chính người chơi.
- Người chơi chọn:
  1) ô kề bên đích đến
  2) số quân muốn di chuyển

Giới hạn di chuyển:
- Không thể di chuyển nếu không có quân ở ô hiện tại.
- Không thể di chuyển số quân vượt quá số quân đang có.
- Không thể di chuyển vượt quá `supply * 100_000` (giới hạn hậu cần).
- Không được di chuyển 0 quân.

## 7.4. Hiến tế một cấp trong hậu cần để đổi lấy quân (chỉ khi thiếu quân)
Chỉ xuất hiện khi điều kiện:
- `troops == 0` (hết quân tổng)

Khi hiến tế:
- `supply -= 1`
- đặt lại `troops = 1_000_000` (tức “được hồi lại” số quân)
- sau đó người chơi vẫn tiếp tục với lượng hậu cần giảm.

> Nếu `supply == 1` thì hành động hiến tế không còn khả dụng và đối thủ thắng theo điều kiện ở mục 6.3.

---

## 8) Cách chơi nhanh (tóm tắt chiến lược)
- Dùng **kinh tế** để có tiền mua nâng cấp.
- Ưu tiên **hiệu suất** để có nhiều hành động mỗi lượt.
- Khi đủ quân: **di chuyển theo đường kề ô** để gây giao tranh ở khu vực của đối thủ.
- Nâng **sát thương/phòng thủ** để tăng khả năng thắng khi giao tranh nổ ra ở các ô.
- Cân nhắc **hậu cần (supply)** vì nó vừa giới hạn di chuyển vừa là tài nguyên để hiến tế.

---
Được folk bởi An

Mô hình AI được sử dụng là Google Gemini 3.1 Flash Lite

Tài liệu được soạn bởi model Minimax M2.7