// 3D animation using Three.js for the calculator UI
import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.153.0/build/three.module.js';

const container = document.createElement('div');
document.body.appendChild(container);
container.style.position = 'fixed';
container.style.top = '0';
container.style.left = '0';
container.style.width = '100vw';
container.style.height = '100vh';
container.style.zIndex = '-1';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);
container.appendChild(renderer.domElement);

// Add a rotating torus knot
const geometry = new THREE.TorusKnotGeometry(2, 0.5, 100, 16);
const material = new THREE.MeshStandardMaterial({ color: 0xfda085, metalness: 0.6, roughness: 0.3 });
const torusKnot = new THREE.Mesh(geometry, material);
scene.add(torusKnot);

// Add some lights
const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
scene.add(ambientLight);
const pointLight = new THREE.PointLight(0xf6d365, 1, 100);
pointLight.position.set(5, 10, 10);
scene.add(pointLight);

camera.position.z = 7;

function animate() {
    requestAnimationFrame(animate);
    torusKnot.rotation.x += 0.01;
    torusKnot.rotation.y += 0.013;
    renderer.render(scene, camera);
}
animate();

window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});
