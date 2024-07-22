import streamlit as st
import requests
from streamlit.components.v1 import html


# Tiêu đề trang web
st.title("Tool gợi ý viết bài chuyên sâu")
if 'edit_state' not in st.session_state:
    st.session_state.edit_state = {}  # Dùng để theo dõi trạng thái chỉnh sửa

if "page" not in st.session_state: 

    # Textbox đầu tiên để nhập tiêu đề bài viết
    article_title = st.text_input("Nhập tiêu đề / chủ đề của bài viết")

    # Chọn đối tượng từ một danh sách hoặc nhập văn bản tùy chỉnh
    options = ["Doanh nghiệp", "Sale", "Marketer", "CSKH"]
    selected_option = st.selectbox("Chọn đối tượng của bài viết", options + ["Khác"])

    if selected_option == "Khác":
        target_audience = st.text_input("Nhập đối tượng mà bài viêt hướng đến.")
    else:
        target_audience = selected_option

    # Textarea để nhập dàn bài chi tiết
    outline = st.text_area("Nhập dàn bài chi tiết", height=300)

    # Tạo một nút màu xanh và dài hết chiều rộng
    st.markdown("""
        <style>
        .stButton>button {
            background-color: #008000; /* Màu xanh */
            color: white;
            width: 100%;
            height: 50px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #006400; /* Màu xanh đậm hơn khi hover */
        }
        </style>
        """, unsafe_allow_html=True)
    # Nút Generate
    if st.button("Generate"):
        # Kiểm tra các trường bắt buộc
        if not article_title:
            st.error("Tiêu đề bài viết là bắt buộc.")
        elif selected_option == "Khác" and not target_audience:
            st.error("Đối tượng là bắt buộc nếu chọn 'Khác'.")
        else:
            result = {
                "Tiêu đề bài viết": article_title,
                "Đối tượng": target_audience,
                "Dàn bài chi tiết": outline
            }
            
            # # Hiển thị kết quả
            # st.write("Kết quả:")
            # st.write(result)
            
            # # Địa chỉ API endpoint
            # api_url = "https://your-api-endpoint.example.com/submit"
            
            
            # try:
            #     # Gửi dữ liệu đến API
            #     response = requests.post(api_url, json=result)
            #     response.raise_for_status()  # Kiểm tra lỗi HTTP
                
            #     # Lưu phản hồi từ API vào session state
            #     st.session_state.api_response = response.json()
                
            #     # Chuyển hướng đến trang kết quả
            #     st.session_state.page = "result"
            #     st.experimental_rerun()
            # except requests.exceptions.RequestException as e:
            #     st.error(f"Đã xảy ra lỗi khi gửi dữ liệu đến API: {e}")


        # Lưu kết quả vào session state
        st.session_state.result = result
        
        # Giả lập phản hồi từ API
        fake_api_response = {
            "outline": outline,
            "result": [
                {
                    "Khác biệt về giao diện và Branding": [
                        "Website giá rẻ, thường chỉ vài triệu đồng, thường sử dụng các mẫu giao diện có sẵn hoặc những thiết kế đơn giản, không có sự tùy chỉnh sâu sắc. Điều này dẫn đến việc giao diện của những trang web này thường không thể hiện được bản sắc riêng của doanh nghiệp. Mặc dù có thể tiết kiệm chi phí ban đầu, nhưng việc sử dụng các mẫu giao diện có sẵn dễ dàng dẫn đến tình trạng website của bạn trông giống với nhiều trang web khác, không tạo được ấn tượng đặc biệt với khách hàng. Điều này có thể làm giảm khả năng nhận diện thương hiệu và không hỗ trợ mạnh mẽ cho các chiến dịch marketing của doanh nghiệp.",
                        "Một giao diện không được đầu tư kỹ lưỡng cũng thường thiếu các yếu tố tối ưu hóa trải nghiệm người dùng (UI/UX). Điều này có thể dẫn đến việc khách hàng gặp khó khăn trong việc tìm kiếm thông tin hoặc thực hiện các thao tác trên website, từ đó làm giảm tỷ lệ chuyển đổi và hiệu quả kinh doanh. Ví dụ, một trang web bán hàng giá rẻ có thể không có các tính năng như thanh toán trực tuyến, hệ thống trò chuyện trực tuyến hay gợi ý cá nhân hóa, khiến trải nghiệm mua sắm của khách hàng không được liền mạch và thuận tiện.",
                        "Ngược lại, một website có chi phí trăm triệu thường được thiết kế độc quyền, dựa trên yêu cầu cụ thể của doanh nghiệp và khách hàng mục tiêu. Điều này giúp trang web không chỉ mang đậm bản sắc thương hiệu mà còn tối ưu hóa trải nghiệm người dùng. Các yếu tố như bố cục, màu sắc, logo và các chi tiết nhỏ khác đều được chăm chút kỹ lưỡng để tạo ra một giao diện ấn tượng, dễ nhận diện và chuyên nghiệp. Một ví dụ điển hình là các website sử dụng công nghệ hiện đại như BizWebsite, cung cấp giao diện đẹp, hiện đại và độc quyền, cùng với khả năng cập nhật các xu hướng thiết kế mới, giúp doanh nghiệp nổi bật giữa đám đông.",
                        "Ngoài ra, một website được đầu tư lớn thường tích hợp các tính năng nâng cao như công cụ thanh toán trực tuyến, hệ thống trò chuyện trực tuyến, gợi ý cá nhân hóa và hỗ trợ đa nền tảng. Những tính năng này không chỉ nâng cao trải nghiệm người dùng mà còn giúp doanh nghiệp dễ dàng quản lý và vận hành website hiệu quả hơn. Ví dụ, các trang web bất động sản sử dụng công nghệ thực tế ảo (VR) hoặc 3D để khách hàng có thể tham quan trực tuyến, mang lại trải nghiệm tương tác chân thực và sống động, từ đó tăng khả năng chốt sale và sự hài lòng của khách hàng.",
                        "Tóm lại, việc đầu tư vào một website có chi phí cao không chỉ mang lại một giao diện đẹp mắt và chuyên nghiệp, mà còn giúp tối ưu hóa trải nghiệm người dùng và hỗ trợ mạnh mẽ cho các chiến dịch marketing. Doanh nghiệp cần cân nhắc kỹ lưỡng giữa chi phí và lợi ích dài hạn để đưa ra quyết định phù hợp với mục tiêu kinh doanh của mình."
                    ]
                },
                {
                    "Khả năng bảo mật": [
                        "Khi doanh nghiệp lựa chọn thiết kế website với chi phí vài triệu đồng, thường các trang web này sẽ được lưu trữ trên các máy chủ công cộng. Đây là các máy chủ chia sẻ, nơi mà nhiều website cùng sử dụng chung tài nguyên như CPU, RAM và băng thông. Việc này dẫn đến tình trạng dễ xảy ra rủi ro về hiệu suất và bảo mật. Khi một trong các website trên cùng máy chủ gặp vấn đề về lưu lượng truy cập lớn hoặc bị tấn công, tất cả các website khác trên cùng máy chủ cũng sẽ bị ảnh hưởng. Điều này có thể dẫn đến tình trạng website chậm, không ổn định hoặc thậm chí là bị gián đoạn hoàn toàn.",
                        "Hơn nữa, việc lưu trữ trên máy chủ công cộng cũng đồng nghĩa với việc doanh nghiệp không có quyền kiểm soát tối đa đối với môi trường lưu trữ của mình. Các máy chủ công cộng thường không được tối ưu hóa cho từng loại mã nguồn cụ thể, dẫn đến hiệu suất hoạt động không đạt được mức tối ưu. Ngoài ra, các biện pháp bảo mật trên máy chủ công cộng thường không được tùy chỉnh cho từng website, mà chỉ áp dụng các biện pháp bảo mật chung chung, dễ bị tấn công và khai thác lỗ hổng. Điều này đặc biệt nguy hiểm đối với các doanh nghiệp kinh doanh trực tuyến, nơi mà dữ liệu khách hàng và giao dịch là vô cùng quan trọng.",
                        "Ngược lại, với các website có chi phí đầu tư lên đến hàng trăm triệu đồng, doanh nghiệp thường sẽ được cung cấp dịch vụ lưu trữ trên máy chủ riêng. Máy chủ riêng là loại máy chủ mà toàn bộ tài nguyên được dành riêng cho một website duy nhất, không chia sẻ với bất kỳ website nào khác. Điều này giúp đảm bảo hiệu suất và độ ổn định cao nhất cho website, ngay cả khi lưu lượng truy cập tăng đột biến. Ví dụ, các tính năng cao cấp như công nghệ 3D, VR, AI có thể hoạt động mượt mà và hiệu quả hơn trên máy chủ riêng, mang lại trải nghiệm tốt nhất cho người dùng.",
                        "Ngoài ra, việc sử dụng máy chủ riêng còn cho phép doanh nghiệp tùy chỉnh môi trường lưu trữ sao cho phù hợp nhất với mã nguồn lập trình của website. Điều này giúp tối ưu hóa hiệu suất và đảm bảo an toàn cho dữ liệu. Các biện pháp bảo mật có thể được thiết kế và triển khai riêng biệt cho từng website, giúp phòng ngừa và xử lý các lỗ hổng bảo mật một cách hiệu quả. Ví dụ, các tiêu chuẩn bảo mật OWASP có thể được áp dụng một cách nghiêm ngặt và tùy chỉnh theo nhu cầu cụ thể của doanh nghiệp, giúp giảm thiểu rủi ro bị tấn công và đánh cắp dữ liệu."
                    ]
                }
            ]
        }
        
        # Lưu phản hồi từ API vào session state
        st.session_state.api_response = fake_api_response
        
        # Chuyển hướng đến trang kết quả
        st.session_state.page = "result"
        st.rerun()

# Kiểm tra nếu session_state có trang 'result'
elif  st.session_state.page == "result":
    

    # # Hiển thị kết quả từ API
    # st.title("Kết quả")
    # st.write("Kết quả gửi dữ liệu:")
    # st.write(st.session_state.result)
    
    # # Hiển thị phản hồi từ API
    # st.write("Phản hồi từ API:")
    # st.write("Dàn bài chi tiết:")
    # st.write(st.session_state.api_response['outline'])
    
    st.write("Kết quả:")
    
    # Hiển thị từng mục kết quả với chức năng chỉnh sửa
    for i, item in enumerate(st.session_state.api_response['result']):
        for heading, paragraphs in item.items():
            st.write(f"**{heading}:**")
            
            for j, paragraph in enumerate(paragraphs):
                st.write(f"**Đoạn văn {j+1}:**")
                st.write(paragraph)
                
                # Tạo một khóa duy nhất cho trạng thái chỉnh sửa của từng đoạn văn
                edit_key = f"edit_{i}_{j}"
                
                if edit_key not in st.session_state:
                    st.session_state[edit_key] = False

                if st.session_state[edit_key]:
                    # Hiển thị textbox và nút Gửi chỉnh sửa
                    comment_key = f"comment_{i}_{j}"
                    comment = st.text_area(f"Nhận xét cho Đoạn văn {j+1}", key=comment_key)
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button(f"Gửi chỉnh sửa_{i}_{j}"):
                            # Gửi yêu cầu đến API (mã giả lập, yêu cầu thật thì comment dòng này)
                            # response = requests.post('https://your-api-endpoint.example.com/submit-edits', json={
                            #     "heading": heading,
                            #     "paragraph": paragraph,
                            #     "comment": comment
                            # })
                            st.success(f"Đã gửi chỉnh sửa cho đoạn văn {j+1}")
                            st.session_state[edit_key] = False
                    with col2:
                        if st.button(f"Hủy chỉnh sửa_{i}_{j}"):
                            st.session_state[edit_key] = False
                
                else:
                    # Sử dụng nút "Cần chỉnh sửa"
                    if st.button(f"Cần chỉnh sửa_{i}_{j}"):
                        st.session_state[edit_key] = True
                
                
else:
    st.error("Trang này không tồn tại.")
