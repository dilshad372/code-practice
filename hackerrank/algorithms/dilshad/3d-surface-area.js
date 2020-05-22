function surfaceArea(A) {

    let arrLen = A.length;
    let len = A[0].length;
    let left = [];
    let right = [];
    let up = [];
    let down = [];
    let temp = [];
    let adjacent = [];
    let x, y;
    let total = 0;
for(let i = 0; i< arrLen; i++){
    for(let j = 0; j < len; j++) {
        left = [i, j-1];
        right = [i, j+1];
        up = [i-1, j];
        down = [i+1, j];
        temp = [left, right, up, down]
        adjacent = [];
        console.log(temp);
        for(let k = 0; k< temp.length; k++)
        {
            x = temp[k][0];
            y = temp[k][1];

            if((x >= 0 && x < arrLen) && (y >= 0 && y < len))
            {
                adjacent.push(A[x][y]);
            }

        }
        let height = A[i][j];
        let area_threshold = ((4-adjacent.length)*height) + 2;

        let temp_sum = 0;

        for (let k = 0; k < adjacent.length; k++)
        {
            if (height > adjacent[k])
            {
                temp_sum += (height - adjacent[k]);
            }
        }

        total += (temp_sum + area_threshold)

    }
}
return total;
}
