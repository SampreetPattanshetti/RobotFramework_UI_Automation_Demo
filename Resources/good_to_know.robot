IF $delete_btn_status == 'PASS
Press Keys    ${None}    ESC
Press Keys    ${None}    Mouse Down
Press Keys    ${None}    BACKSPACE
Press Keys    ${None}    RIGHT (Right arrow key)
Press Keys    None    TAB

${status}    Run Keyword And Ignore Error    wait until element is visible    xpath:
${status}    Set Variable    ${status}[0]
IF    $status == 'PASS'