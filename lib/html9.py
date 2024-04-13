site = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vertical Table With Navbar</title>
    <style>
        body $
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Modern font */
        &
        .navbar $
            background-color: #0088cc; /* Telegram blue */
            padding: 10px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: white;
        &
        .navbar img $
            width: 50px;
            height: 50px;
            border-radius: 50%;
            margin-right: 15px;
        &
        .navbar-text $
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        &
        .navbar-text .bold $
            font-weight: bold;
        &
        .navbar-text .light $
            font-weight: 300;
        &

        .report-section $
            padding: 20px;
            background-color: #f4f4f4;
            margin-top: 0px;
        &
        .report-title $
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
        &
        .report-content $
            font-size: 14px;
            margin-bottom: 20px;
        &
        .output-input $
            width: 100%;
            height: 100px; /* Increased height for better visibility */
            box-sizing: border-box;
            font-size: 16px;
            margin-bottom: 15px;
        &
        table $
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background-color: #fff;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        &
        th, td $
            border: 1px solid #ddd;
            padding: 12px 15px;
            text-align: left;
            vertical-align: middle;
        &
        th $
            background-color: #f9f9f9; /* Lighter color for better visibility */
            font-weight: 600;
        &
        .profile-photo-row img $
            width: 50px;
            height: 50px;
            border-radius: 50%;
        &
        .warning $
            color: red;
            margin-top: 20px;
            font-size: 12px;
        &
    </style>
</head>
<body>
    <div class="navbar">
        <div class="logo-and-text">
            <img src="cid:image1">
            <div class="navbar-text">
                <span class="bold">{}</span>
                <span class="light">({})</span>
            </div>
        </div>
    </div>
    <div class="report-section">
        <div class="report-title">Report Section</div>
        <input type="text" class="output-input" value="{}">
        <div class="report-content">
            This section can contain an explanation regarding the details of the report. You can share the summary or important notes of your report here.
        </div>
        <table>
            <tr>
                <th>Group Name</th>
                <td>{}</td>
            </tr>
            <tr>
                <th>Group ID</th>
                <td>{}</td>
            </tr>
            <tr class="profile-photo-row">
                <th>Profile Photo</th>
                <td><img src="cid:image2"></td>
            </tr>
            <tr>
                <th>Message Owner</th>
                <td>{}</td>
            </tr>
            <tr>
                <th>Sender's ID</th>
                <td>{}</td>
            </tr>
            <tr>
                <th>Sender's Phone Number</th>
                <td>{}</td>
            </tr>
            <tr>
                <th>Images</th>
                <td>
                    <img src="cid:image3">
                </td>
            </tr>
        </table>
        <div class="warning">Warning: Attachments are below.</div>
    </div>
</body>
</html>
'''