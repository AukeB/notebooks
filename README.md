# notebooks
This repository contains all kinds of different notebooks.

let m = [
  [1, 2, 3],
  [4, 5, 6]
];

let n = [
  [1, 2],
  [3, 4],
  [5, 6]
];

let background_color = 255;
let canvasSize = 650;
let cellSize = 0.1 * canvasSize
let borderMargin = 0.08 * canvasSize
let matrixMargin = 0.05 * canvasSize

function setup() {
  createCanvas(canvasSize, canvasSize);
}

function draw() {
  background(background_color);
  
  drawMatrixMultiplicationAnimation(m, n, cellSize, borderMargin, matrixMargin)
}

function drawMatrixMultiplicationAnimation(m, n, cellSize, borderMargin, matrixMargin) {
  let p = math.multiply(m, n);
  
  xM = borderMargin
  yM = borderMargin + cellSize * n.length + matrixMargin
  xN = borderMargin + cellSize * m[0].length + matrixMargin
  yN = borderMargin
  xP = borderMargin + cellSize * m[0].length + matrixMargin
  yP = borderMargin + cellSize * n.length + matrixMargin
  
  //highlightAnimation(m, xM, yM, cellSize, 3);
  drawComputeAnimation(m, xM, yM, cellSize, 3);
  drawMatrix(m, xM, yM, cellSize);
  drawMatrix(n, xN, yN, cellSize);
  drawMatrix(p, xP, yP, cellSize);
}

function drawMatrix(matrix, x, y, cellSize, matrixColor = 0) {
  let rows = matrix.length;
  let cols = matrix[0].length;
  
  let matrixWidth = cols * cellSize;
  let matrixHeight = rows * cellSize;
  
  drawMatrixBrackets(x, y, matrixWidth, matrixHeight, cellSize, matrixColor);
  drawMatrixNumbers(matrix, x, y, rows, cols, cellSize, matrixColor)
}

function drawMatrixBrackets(x, y, matrixWidth, matrixHeight, cellSize, matrixColor, horizontalRatio = 0.075) {
  let bracketWidth = cellSize / 30
  
  stroke(matrixColor);
  fill(matrixColor)
  
  // Vertical lines
  rect(x, y, bracketWidth, matrixHeight)
  rect(x + matrixWidth, y, bracketWidth, matrixHeight);
  
  // Horizontal lines.
  rect(x, y, horizontalRatio * matrixWidth, bracketWidth)
  rect(x + (1 - horizontalRatio) * matrixWidth, y, horizontalRatio * matrixWidth, bracketWidth)
  rect(x, y + matrixHeight - bracketWidth, horizontalRatio * matrixWidth, bracketWidth)
  rect(x + (1 - horizontalRatio) * matrixWidth, y + matrixHeight - bracketWidth, horizontalRatio * matrixWidth, bracketWidth)
}

function drawMatrixNumbers(matrix, x, y, rows, cols, cellSize, matrixColor) {
  textAlign(CENTER, CENTER)
  textSize(cellSize * 0.45)
  fill(matrixColor);
  noStroke();
  
  textFont('serif');
  
  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      let cellX = x + col * cellSize + cellSize / 2;
      let cellY = y + row * cellSize + cellSize / 2;
      
      text(matrix[row][col], cellX, cellY)
    }
  }
}



function highlightAnimation(m, x, y, cellSize, t) {
  let rows = m.length;
  let cols = m[0].length;
  let borderWidth = 10;
  let framesPerHighlight = t * 60;
  
  let currentFrame = frameCount % (framesPerHighlight * rows);
  let currentRow = floor(currentFrame / framesPerHighlight);
  let frameInHighlight = currentFrame % framesPerHighlight;
  let fadeFrames = framesPerHighlight / 10;
  
  let alpha = 0;
  
  if (frameInHighlight < fadeFrames) {
    alpha = map(frameInHighlight, 0, fadeFrames, 0, 255);
  } else if (frameInHighlight > framesPerHighlight - fadeFrames) {
    alpha = map(frameInHighlight, framesPerHighlight - fadeFrames, framesPerHighlight, 255, 0);
  } else {
    alpha = 255;
  }
  
  noStroke();
  fill(255, 255, 119, alpha);
  
  // Highlight the current row
  rect(x + borderWidth, y + borderWidth + currentRow * cellSize, cols * cellSize - 2 * borderWidth, cellSize - 2 * borderWidth, 10);
}

function drawComputeAnimation(matrix, x, y, cellSize, t) {
  let cols = matrix[0].length;
  let rows = matrix.length;
  
  // Total frames for the animation
  let totalFrames = t * 60;
  let currentFrame = frameCount % totalFrames;
  let progress = currentFrame / totalFrames;  // 0 to 1 progress
  
  textAlign(CENTER, CENTER);
  textSize(cellSize * 0.45);
  fill(0);
  noStroke();
  textFont('serif');
  
  // Animate only the first row digits moving to (0,0) of the result matrix
  for (let col = 0; col < cols; col++) {
    // Start position (in the matrix m)
    let startX = x + col * cellSize + cellSize / 2;
    let startY = y + 0 * cellSize + cellSize / 2;
    
    // End position is always the first cell (0,0) of the result matrix (assumed at x,y)
    // So endX and endY both equal to the center of cell (0,0)
    let endX = x + cellSize / 2;
    let endY = y + cellSize / 2;
    
    // Linear interpolation between start and end positions
    let currentX = lerp(startX, endX, progress);
    let currentY = lerp(startY, endY, progress);
    
    text(matrix[0][col], currentX +10, currentY);
  }
}
