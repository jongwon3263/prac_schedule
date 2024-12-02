document.addEventListener('DOMContentLoaded', function() {
    const companySelect = document.getElementById('company-filter');
    const scheduleRows = document.querySelectorAll('.schedule-row');

    // 업체 드롭다운 선택 시
    companySelect.addEventListener('change', function() {
        const selectedCompany = companySelect.value;
        updateFilters(selectedCompany);
    });

    // 업체 선택에 따른 필터 업데이트 함수
    function updateFilters(selectedCompany) {
        scheduleRows.forEach(row => {
            const company = row.querySelector('td:nth-child(9)').textContent.trim(); // 업체 이름 (9번째 컬럼)

            // 선택된 업체와 행의 업체가 일치하면 표시, 아니면 숨기기
            if (selectedCompany === "" || company === selectedCompany) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    }
});
